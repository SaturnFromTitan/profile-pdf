module.exports = {
  plugins: [
    require('postcss-import'),
    // Custom plugin to remove @layer directives as it's not supported by WeasyPrint
    {
      postcssPlugin: 'remove-layers',
      AtRule: {
        layer: (atRule) => {
          // Remove @layer directives by replacing them with their contents
          atRule.replaceWith(atRule.nodes || []);
        }
      }
    },
    // Custom plugin to dynamically resolve CSS custom properties (var) as it's not supported by WeasyPrint
    {
      postcssPlugin: 'resolve-vars-dynamic',
      Once(root) {
        // First pass: collect all variable definitions
        const variables = new Map();

        root.walkDecls((decl) => {
          if (decl.prop && decl.prop.startsWith('--')) {
            variables.set(decl.prop, decl.value);
          }
        });

        // Second pass: resolve var() functions
        let changed = true;
        let iterations = 0;
        const maxIterations = 10; // Prevent infinite loops

        while (changed && iterations < maxIterations) {
          changed = false;
          iterations++;

          root.walkDecls((decl) => {
            if (decl.value && decl.value.includes('var(')) {
              let resolvedValue = decl.value;

              // Replace all var() functions with their actual values
              variables.forEach((value, prop) => {
                const regex = new RegExp(`var\\(${prop.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}(?:,\\s*([^)]+))?\\)`, 'g');
                resolvedValue = resolvedValue.replace(regex, (match, fallback) => {
                  // If the variable exists, use it; otherwise use the fallback
                  return variables.has(prop) ? variables.get(prop) : (fallback || '');
                });
              });

              if (resolvedValue !== decl.value) {
                decl.value = resolvedValue;
                changed = true;
              }
            }
          });
        }

        // Final pass: resolve any remaining var() functions with fallbacks
        root.walkDecls((decl) => {
          if (decl.value && decl.value.includes('var(')) {
            decl.value = decl.value.replace(/var\([^,)]+(?:,\s*([^)]+))?\)/g, (match, fallback) => {
              return fallback || '';
            });
          }
        });
      }
    }
  ]
};
