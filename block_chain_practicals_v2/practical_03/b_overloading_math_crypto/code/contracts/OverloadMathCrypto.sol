// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.20;

contract OverloadMathCrypto {
    function sum(uint256 a, uint256 b) external pure returns (uint256) {
        return a + b;
    }

    function sum(uint256 a, uint256 b, uint256 c) external pure returns (uint256) {
        return a + b + c;
    }

    function hashKeccak(bytes memory data) external pure returns (bytes32) {
        return keccak256(data);
    }

    function hashSha256(bytes memory data) external pure returns (bytes32) {
        return sha256(data);
    }

    function hashRipemd160(bytes memory data) external pure returns (bytes20) {
        return ripemd160(data);
    }
}
