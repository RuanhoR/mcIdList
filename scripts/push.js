const fs = require("node:fs/promises");
const path = require("node:path");
async function fileExists(filePath) {
  try {
    await fs.stat(filePath);
  } catch {
    return false;
  }
  return true;
}
async function main() {
  const target = process.argv[2];
  const platform = process.argv[3];
  if (!target) {
    return console.error("Err: No target");
  }
  if (!platform || (platform !== "be" && platform !== "je")) {
    return console.error("Err: No platform");
  }
  if (!(await fileExists(path.resolve(`./data/${platform}_${target}.json`)))) {
    return console.error("Cannot resolve");
  }
  const pgJSON = JSON.parse(await fs.readFile(path.resolve("package.json")));
  pgJSON.name = `@ojaang/${platform}-vanilla-iddata`;
  pgJSON.version = target;
  pgJSON.files[0] = `./data/${platform}_${target}.json`;
  await fs.writeFile(
    path.resolve("index.js"),
    `module.exports = require("./data/${platform}_${target}.json");`,
  );
  await fs.writeFile(
    path.resolve("package.json"),
    JSON.stringify(pgJSON, null, 2),
  );
  await fs.writeFile(
    path.resolve("index.d.ts"),
    `import e = require("./data/${platform}_${target}.json");
export = e;`,
  );
}
main();
