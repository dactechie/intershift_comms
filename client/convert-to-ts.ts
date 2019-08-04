import sqlts from '@rmp135/sql-ts'

const config = {
    "dialect":"sqlite",
    "connection": {
      "host": "localhost",
      "filename": "../server/apis/handover.db",
      //"database" : "../server/apis/handover.db"
    }
};

async function runme() {
  const definitions = await sqlts.toTypeScript(config);
  console.log(definitions);
}

runme();
