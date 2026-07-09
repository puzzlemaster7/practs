// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.20;

/**
 * Minimal ERC-721-like NFT for lab/demo usage only.
 * - Enough to mint, read ownerOf, and transfer.
 * - Not a complete ERC-721 implementation (no safeTransfer checks, metadata, etc).
 */
contract BasicNFT {
    string public name;
    string public symbol;

    mapping(uint256 => address) private _ownerOf;
    mapping(address => uint256) private _balanceOf;
    mapping(uint256 => address) private _approved;

    event Transfer(address indexed from, address indexed to, uint256 indexed tokenId);
    event Approval(address indexed owner, address indexed approved, uint256 indexed tokenId);

    constructor(string memory _name, string memory _symbol) {
        name = _name;
        symbol = _symbol;
    }

    function ownerOf(uint256 tokenId) external view returns (address) {
        address owner = _ownerOf[tokenId];
        require(owner != address(0), "NOT_MINTED");
        return owner;
    }

    function balanceOf(address owner) external view returns (uint256) {
        require(owner != address(0), "ZERO_ADDRESS");
        return _balanceOf[owner];
    }

    function getApproved(uint256 tokenId) external view returns (address) {
        require(_ownerOf[tokenId] != address(0), "NOT_MINTED");
        return _approved[tokenId];
    }

    function approve(address to, uint256 tokenId) external {
        address owner = _ownerOf[tokenId];
        require(owner != address(0), "NOT_MINTED");
        require(msg.sender == owner, "NOT_OWNER");
        _approved[tokenId] = to;
        emit Approval(owner, to, tokenId);
    }

    function transferFrom(address from, address to, uint256 tokenId) public {
        address owner = _ownerOf[tokenId];
        require(owner != address(0), "NOT_MINTED");
        require(owner == from, "FROM_NOT_OWNER");
        require(to != address(0), "ZERO_ADDRESS");
        require(msg.sender == owner || msg.sender == _approved[tokenId], "NOT_AUTHORIZED");

        _approved[tokenId] = address(0);
        _ownerOf[tokenId] = to;
        _balanceOf[from] -= 1;
        _balanceOf[to] += 1;
        emit Transfer(from, to, tokenId);
    }

    function mint(address to, uint256 tokenId) external {
        require(to != address(0), "ZERO_ADDRESS");
        require(_ownerOf[tokenId] == address(0), "ALREADY_MINTED");
        _ownerOf[tokenId] = to;
        _balanceOf[to] += 1;
        emit Transfer(address(0), to, tokenId);
    }
}

