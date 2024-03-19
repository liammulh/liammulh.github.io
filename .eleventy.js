const INPUT_DIR = "_src";
const OUTPUT_DIR = "_dist";

module.exports = function (eleventyConfig) {
    eleventyConfig.addPassthroughCopy(`${INPUT_DIR}/CNAME`);
    eleventyConfig.addPassthroughCopy(`${INPUT_DIR}/burp.css`);
    return {
        dir: {
            input: INPUT_DIR,
            output: OUTPUT_DIR
        }
    }
};
