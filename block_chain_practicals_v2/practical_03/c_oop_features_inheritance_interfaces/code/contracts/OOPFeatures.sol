// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.20;

interface IGreeter {
    function greet() external view returns (string memory);
}

abstract contract BaseCounter {
    uint256 internal count;

    constructor(uint256 initial) {
        count = initial;
    }

    function getCount() external view returns (uint256) {
        return count;
    }

    function increment() external virtual;
}

contract Counter is BaseCounter, IGreeter {
    constructor(uint256 initial) BaseCounter(initial) {}

    function increment() external override {
        count += 1;
    }

    function greet() external pure override returns (string memory) {
        return "hello";
    }
}
