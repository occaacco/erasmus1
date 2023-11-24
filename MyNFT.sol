// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MyNFT is ERC1155, Ownable {
    struct NFT {
        string name;
        string description;
        string imageHash;
    }

    mapping(uint256 => NFT) public nfts;
    event NFTCreated(uint256 indexed tokenId, string name, string description, string imageHash);
    uint256 private nextTokenId;

    constructor() ERC1155("https://ipfs.io/ipfs/Qmf3whjtx6UnNcZLCHcYVqj6DkLWLpAbQJnaT1iPpBe5vZ?filename=something.json") Ownable(msg.sender) {
        Ownable.transferOwnership(msg.sender);
    }

    function createNFT() external onlyOwner {
        string memory name = "Test NFT";
        string memory description = "It is a test description";
        string memory imageHash = "https://ipfs.io/ipfs/QmeeKjFdBjfjtsuRVj8zFqPrmaztF73R5G9BDo3cxDuPGD";

        nfts[nextTokenId] = NFT(name, description, imageHash);
        uint256 tokenId = nextTokenId++;

        _mint(msg.sender, tokenId, 1, "");
        emit NFTCreated(tokenId, name, description, imageHash);
    }
}
