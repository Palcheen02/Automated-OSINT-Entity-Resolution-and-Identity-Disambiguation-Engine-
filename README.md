# Automated-OSINT-Entity-Resolution-and-Identity-Disambiguation-Engine-
An automated OSINT engine for identity disambiguation and digital footprint analysis. Built for cybercrime investigations.
# Vanguard OSINT Engine 🎯

A Python-based open-source intelligence prototype designed to automate identity resolution during cyber investigations. 

Instead of manual data scraping, this engine takes fragmented suspect data (like a real name), dynamically generates hundreds of highly probable username permutations, and cross-references them against public APIs. It utilizes a custom scoring algorithm to filter out false positives and isolate the verified target.

### Core Features
* **Automated Permutation Generation:** Creates 150+ logical username combinations instantly.
* **Identity Disambiguation Scoring:** Computes a 0-100 confidence score based on known seed data.
* **Automated Evidence Exporting:** Generates hard-copy `.txt` intelligence reports for case files.

*Note: This is a Proof of Concept (PoC) built for law enforcement research presentations.*
