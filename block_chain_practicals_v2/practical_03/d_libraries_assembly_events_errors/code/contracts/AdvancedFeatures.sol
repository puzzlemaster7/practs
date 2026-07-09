// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.20;

library MathLib {
    function double(uint256 x) internal pure returns (uint256) {
        return x * 2;
    }
}

error ValueTooSmall(uint256 provided, uint256 minRequired);

contract AdvancedFeatures {
    using MathLib for uint256;

    event ValueSet(address indexed setter, uint256 value);

    uint256 public value;

    function setValue(uint256 newValue) external {
        if (newValue < 1) revert ValueTooSmall(newValue, 1);
        value = newValue;
        emit ValueSet(msg.sender, newValue);
    }

    function doubledValue() external view returns (uint256) {
        return value.double();
    }

    function addAsm(uint256 a, uint256 b) external pure returns (uint256 c) {
        assembly {
            c := add(a, b)
        }
    }
}
