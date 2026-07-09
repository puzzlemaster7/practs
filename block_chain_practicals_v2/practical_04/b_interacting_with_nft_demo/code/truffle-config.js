module.exports = {
  contracts_directory: "./contracts",
  migrations_directory: "./migrations",
  contracts_build_directory: "../output/build/contracts",
  networks: {
    development: {
      host: "127.0.0.1",
      port: 8545,
      network_id: "*"
    }
  },
  compilers: {
    solc: {
      version: "0.8.20"
    }
  }
};

