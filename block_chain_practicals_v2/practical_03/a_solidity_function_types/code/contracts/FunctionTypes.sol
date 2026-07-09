// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.20;

contract FunctionTypes {
    uint256 private value;

    function setValue(uint256 newValue) external {
        value = newValue;
    }

    function getValue() external view returns (uint256) {
        return value;
    }

    function add(uint256 a, uint256 b) external pure returns (uint256) {
        return a + b;
    }

    receive() external payable {}

    fallback() external payable {}
}
