const Counter = artifacts.require("Counter");

module.exports = function (deployer) {
  // Counter has a constructor(uint256 initial)
  deployer.deploy(Counter, 10);
};

