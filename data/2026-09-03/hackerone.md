# HackerOne Public Reports Snapshot

Generated: 2026-09-03T17:08:44.750752+00:00

1. [TaskProcessing callback authorization bypass allows ex-members to post as Assistant Talk Bot](https://hackerone.com/reports/3799010)
   - Program: Nextcloud | Upvotes: 24 | Bounty: $0.00 | Type: Insecure Direct Object Reference (IDOR)
2. [Windows SSPI connection-pool probe can reuse a connection under the wrong user](https://hackerone.com/reports/3938185)
   - Program: curl | Upvotes: 12 | Bounty: $0.00 | Type: Authentication Bypass by Spoofing
3. [libcurl cache updates follow symlinks and truncate their targets](https://hackerone.com/reports/3938220)
   - Program: curl | Upvotes: 3 | Bounty: $0.00 | Type: Time-of-check Time-of-use (TOCTOU) Race Condition
4. [Cookie jar load skips public suffix check on PSL builds](https://hackerone.com/reports/3920276)
   - Program: curl | Upvotes: 6 | Bounty: $0.00 | Type: Information Exposure Through Sent Data
5. [Debug Deep Link Abuse Allows Repeated Forced Logout and Application Disruption](https://hackerone.com/reports/3829030)
   - Program: Yelp | Upvotes: 29 | Bounty: $0.00 | Type: Violation of Secure Design Principles
6. [JaaS SIP Gateway Authorization Bypass](https://hackerone.com/reports/3837634)
   - Program: 8x8 | Upvotes: 43 | Bounty: $500.00 | Type: Missing Authorization
7. [Myndr CORS Misconfiguration](https://hackerone.com/reports/3930957)
   - Program: Myndr | Upvotes: 25 | Bounty: $0.00 | Type: Improper Access Control - Generic
8. [Adding phone number to profile By OTP brute forcing](https://hackerone.com/reports/3265780)
   - Program: CoinMate.io | Upvotes: 87 | Bounty: $100.00 | Type: Insecure Storage of Sensitive Information
9. [URL API: triple-slash parses path segment as hostname](https://hackerone.com/reports/3923212)
   - Program: curl | Upvotes: 24 | Bounty: $0.00 | Type: Use of Incorrectly-Resolved Name or Reference
10. [[Wii U/3DS/Switch] Improper bounds check in StationURL in all NEX clients leading to remote crash/RCE](https://hackerone.com/reports/2551512)
   - Program: Nintendo | Upvotes: 32 | Bounty: $0.00 | Type: Stack Overflow
11. [Unauthenticated RCE in Taskcluster web-server via GraphQL filter argument (sift $where)](https://hackerone.com/reports/3782701)
   - Program: Mozilla | Upvotes: 270 | Bounty: $12000.00 | Type: Code Injection
12. [curl Missing Sec-WebSocket-Accept Verification Enables MITM WebSocket Session Hijacking](https://hackerone.com/reports/3917775)
   - Program: curl | Upvotes: 31 | Bounty: $0.00 | Type: Man-in-the-Middle
13. [`check_reserve_proof` counts duplicate entries: one output can inflate `total`](https://hackerone.com/reports/3699522)
   - Program: Monero | Upvotes: 38 | Bounty: $0.00 | Type: Business Logic Errors
14. [`check_reserve_proof` sums RingCT ECDH amounts without checking the output commitment](https://hackerone.com/reports/3698862)
   - Program: Monero | Upvotes: 33 | Bounty: $0.00 | Type: Missing Required Cryptographic Step
15. [wallet-rpc crash via malformed /gettransactions response (empty txs → vector::front() in check_tx_key / check_tx_proof)](https://hackerone.com/reports/3693636)
   - Program: Monero | Upvotes: 37 | Bounty: $0.00 | Type: NULL Pointer Dereference
16. [SpendProofV1 txid-substitution: get_spend_proof/check_spend_proof do not verify returned transaction hash](https://hackerone.com/reports/3700036)
   - Program: Monero | Upvotes: 26 | Bounty: $0.00 | Type: Missing Required Cryptographic Step
17. [wallet-rpc describe_transfer uses real_output_in_tx_index instead of real_output: cold-wallet pre-sign review shows wrong ring member](https://hackerone.com/reports/3723315)
   - Program: Monero | Upvotes: 17 | Bounty: $0.00 | Type: Array Index Underflow
18. [`set_daemon` wallet-rpc silently ignores `ssl_allowed_fingerprints` → pinning bypassed, wallet↔daemon MITM](https://hackerone.com/reports/3686259)
   - Program: Monero | Upvotes: 1 | Bounty: $0.00 | Type: Improper Certificate Validation
19. [`relay_tx` wallet-rpc skips `--restricted-rpc` guard and lets any caller corrupt wallet state via attacker-controlled `pending_tx`](https://hackerone.com/reports/3687543)
   - Program: Monero | Upvotes: 17 | Bounty: $0.00 | Type: Improper Access Control - Generic
20. [Heap use-after-free (write) in mev_forget_socket() via reentrant curl_easy_pause() — incomplete fix for CVE-2026-9080](https://hackerone.com/reports/3911968)
   - Program: curl | Upvotes: 9 | Bounty: $0.00 | Type: Use After Free
21. [GitHub Retired UsernameTakeover From  [aws/████████]](https://hackerone.com/reports/3478646)
   - Program: AWS VDP | Upvotes: 37 | Bounty: $0.00 | Type: Inclusion of Functionality from Untrusted Control Sphere
22. [Unauthenticated Path Traversal (LFI) via /custom-sounds/ when CustomSounds uses FileSystem storage](https://hackerone.com/reports/3514640)
   - Program: Rocket.Chat | Upvotes: 38 | Bounty: $0.00 | Type: Path Traversal
23. [SMTP CRLF injection in custom SMTP recipient operand allows additional SMTP commands after authentication](https://hackerone.com/reports/3911605)
   - Program: curl | Upvotes: 16 | Bounty: $0.00 | Type: CRLF Injection
24. [Unauthenticated team "income/payments" export ignores donor privacy settings (hide_giving, hide_from_lists) and uses frozen visibility, exposing donat](https://hackerone.com/reports/3878586)
   - Program: Liberapay | Upvotes: 58 | Bounty: $100.00 | Type: 
25. [HTTP Request Smuggling via Connection: close<TAB> in Node.js llhttp parser](https://hackerone.com/reports/3723248)
   - Program: Node.js | Upvotes: 46 | Bounty: $0.00 | Type: HTTP Request Smuggling
26. [Stored XSS in nameserver field on account settings page](https://hackerone.com/reports/3644182)
   - Program: Tucows (VDP) | Upvotes: 48 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Stored
27. [Stored XSS via SVG Upload — check_content() Blocklist Bypass & 256-Byte Scan Limit (Self-Propagating Worm)](https://hackerone.com/reports/3606773)
   - Program: phpBB | Upvotes: 48 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Stored
28. [Permission Model bypass: process.report writes (and overwrites) files outside --allow-fs-write paths](https://hackerone.com/reports/3815767)
   - Program: Node.js | Upvotes: 34 | Bounty: $0.00 | Type: Improper Access Control - Generic
29. [Active Storage Vips Transformer Missing validate_transformation — CVE-2025-24293 Incomplete Fix](https://hackerone.com/reports/3553340)
   - Program: Ruby on Rails | Upvotes: 24 | Bounty: $0.00 | Type: Path Traversal
30. [HTTPS Agent TLS session reuse skips hostname verification across identity policies (incomplete fix of CVE-2026-48934)](https://hackerone.com/reports/3812439)
   - Program: Node.js | Upvotes: 36 | Bounty: $0.00 | Type: Exploiting Incorrectly Configured SSL/TLS
31. [GitHub scoped user to server tokens can escape their installation](https://hackerone.com/reports/3638909)
   - Program: GitHub | Upvotes: 67 | Bounty: $0.00 | Type: Improper Access Control - Generic
32. [Permission Model: --allow-fs-read/--allow-fs-write radix-tree prefix-boundary over-grant](https://hackerone.com/reports/3761342)
   - Program: Node.js | Upvotes: 30 | Bounty: $0.00 | Type: Improper Access Control - Generic
33. [`exportReportPdf` mutation shows internal Activity](https://hackerone.com/reports/3577216)
   - Program: HackerOne | Upvotes: 67 | Bounty: $0.00 | Type: 
34. [HTTPS Agent PFX object-array key collision allows mTLS client identity reuse across different per-request certificates](https://hackerone.com/reports/3816840)
   - Program: Node.js | Upvotes: 23 | Bounty: $0.00 | Type: Improper Authentication - Generic
35. [Permission Model Bypass: `trace_events.createTracing().enable()` Writes Trace Logs Outside `--allow-fs-write`](https://hackerone.com/reports/3838601)
   - Program: Node.js | Upvotes: 19 | Bounty: $0.00 | Type: Improper Access Control - Generic
36. [Unauthenticated SSRF in Voxtelesys integration ('checkUrlForSsrf' Bypass via DNS rebinding)](https://hackerone.com/reports/3473145)
   - Program: Rocket.Chat | Upvotes: 23 | Bounty: $0.00 | Type: Server-Side Request Forgery (SSRF)
37. [Sandbox User Can Inject Rogue CA Certificate into OS Trust Store via Sudo-Allowed deploy-certificates.sh](https://hackerone.com/reports/3633146)
   - Program: AWS VDP | Upvotes: 15 | Bounty: $0.00 | Type: Improper Certificate Validation
38. [Non-Production API Endpoints for the Amazon Cloudwatch Fails to Log to CloudTrail Resulting in Silent Permission Enumeration](https://hackerone.com/reports/3775702)
   - Program: AWS VDP | Upvotes: 17 | Bounty: $0.00 | Type: Insufficient Logging
39. [Authentication Bypass via XML Signature Wrapping in SAML SSO](https://hackerone.com/reports/3827674)
   - Program: Rocket.Chat | Upvotes: 35 | Bounty: $0.00 | Type: Improper Authentication - Generic
40. [ZMQ RPC Log Injection and Untrusted Payload Persistence](https://hackerone.com/reports/3621606)
   - Program: Monero | Upvotes: 30 | Bounty: $0.00 | Type: CRLF Injection
41. [AWS *.a2z.com | Unauthenticated Clickhouse UI : Database access + SSRF](https://hackerone.com/reports/3809407)
   - Program: AWS VDP | Upvotes: 52 | Bounty: $0.00 | Type: Authentication Bypass
42. [GitHub user to server tokens can create issues in any public repository](https://hackerone.com/reports/3641229)
   - Program: GitHub | Upvotes: 57 | Bounty: $0.00 | Type: Improper Access Control - Generic
43. [connect.8x8.com/api/v1: JWT Algorithm Confusion Vulnerability](https://hackerone.com/reports/3800870)
   - Program: 8x8 | Upvotes: 97 | Bounty: $1337.00 | Type: Improper Verification of Cryptographic Signature
44. [OAuth redirect uri validation bypass for :proxima_first_party_sync apps](https://hackerone.com/reports/3588801)
   - Program: GitHub | Upvotes: 74 | Bounty: $0.00 | Type: Open Redirect
45. [Restricted RPC leaks alternative block hashes via /get_alt_blocks_hashes](https://hackerone.com/reports/3738727)
   - Program: Monero | Upvotes: 50 | Bounty: $0.00 | Type: Improper Access Control - Generic
46. [Stored XSS in Rocket.Chat HTML File Export — Unauthenticated Entry via LiveChat](https://hackerone.com/reports/3779690)
   - Program: Rocket.Chat | Upvotes: 93 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Stored
47. [Able to bypass authorization logic and gain more access then intended](https://hackerone.com/reports/3713965)
   - Program: GitHub | Upvotes: 102 | Bounty: $0.00 | Type: 
48. [Bedrock AgentCore Starter Toolkit Creates Gateway IAM Roles Without Confused Deputy Protections](https://hackerone.com/reports/3632577)
   - Program: AWS VDP | Upvotes: 47 | Bounty: $0.00 | Type: Incorrect Permission Assignment for Critical Resource
49. [Stored XSS on Trix Editor version latest (2.1.16) - Sanitizer Bypass](https://hackerone.com/reports/3581911)
   - Program: Basecamp | Upvotes: 83 | Bounty: $337.00 | Type: Cross-site Scripting (XSS) - Stored
50. [bedrock-mantle.api.aws accepts Bedrock API keys outside the IAM Deny, CloudTrail signal, and invocation logging AWS publishes for Bedrock keys](https://hackerone.com/reports/3702072)
   - Program: AWS VDP | Upvotes: 44 | Bounty: $0.00 | Type: Insecure Default Initialization of Resource
51. [SELECT ... INTO OUTFILE does not enforce the FILE WRITE privilege  unprivileged arbitrary file write on the   server](https://hackerone.com/reports/3780695)
   - Program: SingleStore | Upvotes: 48 | Bounty: $0.00 | Type: Missing Authorization
52. [Kiro IDE Stores Auth Tokens with World-Readable Permissions (0644)](https://hackerone.com/reports/3630605)
   - Program: AWS VDP | Upvotes: 54 | Bounty: $0.00 | Type: Incorrect Default Permissions
53. [OS Command Injection in `aws-cdk-lib` NodejsFunction via Unsanitized `OsCommand` Helper (Supply Chain RCE)](https://hackerone.com/reports/3637898)
   - Program: AWS VDP | Upvotes: 108 | Bounty: $0.00 | Type: OS Command Injection
54. [Any installed app can force immediate logout and persistent DOS of authenticated Basecamp sessions via unprotected exported StartActivity](https://hackerone.com/reports/3764217)
   - Program: Basecamp | Upvotes: 101 | Bounty: $287.00 | Type: Improper Access Control - Generic
55. [admin.shopify.com: Shopify Flow continues sending internal emails to a configured recipient after the staff author is removed](https://hackerone.com/reports/3628961)
   - Program: Shopify | Upvotes: 75 | Bounty: $0.00 | Type: 
56. [Non-Production API Endpoints for the Amazon S3 Tables Service Fails to Log to CloudTrail Resulting in Silent Permission Enumeration](https://hackerone.com/reports/3780277)
   - Program: AWS VDP | Upvotes: 68 | Bounty: $0.00 | Type: Insufficient Logging
57. [jitsi-meet: Prosody/Jigasi missing header whitelist in mod_filter_iq_rayo allows arbitrary SIP header injection and Caller ID spoofing](https://hackerone.com/reports/3789570)
   - Program: 8x8 | Upvotes: 71 | Bounty: $100.00 | Type: Improper Input Validation
58. [jitsi-call-analytics: Unauthenticated arbitrary file write via path traversal in `/api/v1/uploads/analyze`](https://hackerone.com/reports/3485343)
   - Program: 8x8 | Upvotes: 66 | Bounty: $100.00 | Type: Path Traversal
59. [Yelp for Business: locked Email field silently editable via API](https://hackerone.com/reports/3766455)
   - Program: Yelp | Upvotes: 73 | Bounty: $0.00 | Type: Client-Side Enforcement of Server-Side Security
60. [Splatoon 3 In-Match Integrity Bypass via Consensus Reflection Attack on Unordered Peer Submission](https://hackerone.com/reports/3559522)
   - Program: Nintendo | Upvotes: 59 | Bounty: $0.00 | Type: Client-Side Enforcement of Server-Side Security
61. [[Splatoon 3] Kick other players with NplnLogin message](https://hackerone.com/reports/3813932)
   - Program: Nintendo | Upvotes: 32 | Bounty: $0.00 | Type: Improper Access Control - Generic
62. [Exceeding the maximum number of spaces allowed by exploiting a Race Condition in the Workspace creation process](https://hackerone.com/reports/3295500)
   - Program: SingleStore | Upvotes: 34 | Bounty: $0.00 | Type: Business Logic Errors
63. [Insecure Direct Object Reference (IDOR) allows creating folders.](https://hackerone.com/reports/3353057)
   - Program: SingleStore | Upvotes: 32 | Bounty: $0.00 | Type: Insecure Direct Object Reference (IDOR)
64. [Delete any folder for any user within the organization](https://hackerone.com/reports/3353035)
   - Program: SingleStore | Upvotes: 31 | Bounty: $0.00 | Type: Insecure Direct Object Reference (IDOR)
65. [Privilege Escalation – Access to the Alert Subscribers page for users with low privileges](https://hackerone.com/reports/3353000)
   - Program: SingleStore | Upvotes: 26 | Bounty: $0.00 | Type: Privilege Escalation
66. [Improper Input Validation — HTTP Response Parser Unconditionally Accepts Bare CR in Status Line](https://hackerone.com/reports/3648681)
   - Program: Node.js | Upvotes: 28 | Bounty: $0.00 | Type: HTTP Request Smuggling
67. [heap-use-after-free in curl_easy_cleanup() called from callback](https://hackerone.com/reports/3833577)
   - Program: curl | Upvotes: 13 | Bounty: $0.00 | Type: Use After Free
68. [setopt(VERIFYPEER) from callback bypasses TLS verify on connection reuse](https://hackerone.com/reports/3831432)
   - Program: curl | Upvotes: 7 | Bounty: $0.00 | Type: 
69. [ssh_config_matches is dead code: unauthorized SSH key reuse](https://hackerone.com/reports/3826843)
   - Program: curl | Upvotes: 11 | Bounty: $0.00 | Type: Authentication Bypass by Primary Weakness
70. [CURLSHOPT_UNSHARE race can cause UAF in shared SSL session cache during HTTPS transfer](https://hackerone.com/reports/3831345)
   - Program: curl | Upvotes: 3 | Bounty: $0.00 | Type: Use After Free
71. [libcurl upload read callbacks miss recursive API guard, allowing prohibited multi API reentry and ASAN-confirmed UAF](https://hackerone.com/reports/3832393)
   - Program: curl | Upvotes: 2 | Bounty: $0.00 | Type: 
72. [Denial of Service (DoS) Vulnerability in Drafts Creation Endpoint](https://hackerone.com/reports/3400140)
   - Program: Discourse | Upvotes: 92 | Bounty: $1024.00 | Type: Uncontrolled Resource Consumption
73. [Inverted ternary in peerlist_manager::filter() allows unlimited whitelist entries per host via different ports](https://hackerone.com/reports/3547349)
   - Program: Monero | Upvotes: 18 | Bounty: $0.00 | Type: 
74. [Remote node DOS](https://hackerone.com/reports/876530)
   - Program: Monero | Upvotes: 24 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
75. [UAF read in mev_pollset_diff() trace path after curl_easy_pause() in socket callback](https://hackerone.com/reports/3824303)
   - Program: curl | Upvotes: 19 | Bounty: $0.00 | Type: Use After Free
76. [Use-after-free in `mev_forget_socket` when `curl_easy_pause()` is called from a `CURL_POLL_REMOVE` socket callback (incomplete fix of CVE-2026-9080)](https://hackerone.com/reports/3823985)
   - Program: curl | Upvotes: 13 | Bounty: $0.00 | Type: Use After Free
77. [mbedTLS / wolfSSL / rustls backends silently skip hostname verification when CURLOPT_SSL_VERIFYPEER=0](https://hackerone.com/reports/3826199)
   - Program: curl | Upvotes: 18 | Bounty: $0.00 | Type: Improper Validation of Certificate with Host Mismatch
78. [CURLOPT_HAPROXY_CLIENT_IP lacks input validation, enabling HAProxy PROXY protocol injection](https://hackerone.com/reports/3823932)
   - Program: curl | Upvotes: 13 | Bounty: $0.00 | Type: CRLF Injection
79. [PHP code injection in delivery-limitation `logical` validation bypass - XML-RPC setChannelTargeting](https://hackerone.com/reports/3781492)
   - Program: Revive Adserver | Upvotes: 45 | Bounty: $0.00 | Type: Code Injection
80. [XML‑RPC login leak exposes valid session ID enabling unauthorized API access](https://hackerone.com/reports/3783738)
   - Program: Revive Adserver | Upvotes: 27 | Bounty: $0.00 | Type: Improper Access Control - Generic
81. [Reflected XSS via unsanitised refresh parameter in zone invocation tag](https://hackerone.com/reports/3780806)
   - Program: Revive Adserver | Upvotes: 28 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
82. [PHP code injection in delivery-limitation `logical` validation bypass](https://hackerone.com/reports/3780854)
   - Program: Revive Adserver | Upvotes: 33 | Bounty: $0.00 | Type: Code Injection
83. [Stored XSS in maintenance tools via unescaped entity names](https://hackerone.com/reports/3781311)
   - Program: Revive Adserver | Upvotes: 24 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Stored
84. [CSRF in zone‑include.php allows unauthorized banner and campaign linking](https://hackerone.com/reports/3781691)
   - Program: Revive Adserver | Upvotes: 19 | Bounty: $0.00 | Type: Cross-Site Request Forgery (CSRF)
85. [Missing ownership validation allows cross‑manager tracker–campaign linking](https://hackerone.com/reports/3780709)
   - Program: Revive Adserver | Upvotes: 17 | Bounty: $0.00 | Type: Insecure Direct Object Reference (IDOR)
86. [Reflected XSS in stats‑video.php via improperly encoded URL parameters](https://hackerone.com/reports/3793243)
   - Program: Revive Adserver | Upvotes: 10 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
87. [HTTP Response Queue Poisoning via TOCTOU Race Condition in `http.Agent`](https://hackerone.com/reports/3582376)
   - Program: Node.js | Upvotes: 11 | Bounty: $0.00 | Type: Time-of-check Time-of-use (TOCTOU) Race Condition
88. [Unix domain socket server bypasses --permission network restrictions (incomplete CVE-2026-21636 fix)](https://hackerone.com/reports/3618831)
   - Program: Node.js | Upvotes: 8 | Bounty: $0.00 | Type: Improper Access Control - Generic
89. [Node.js unicode dot separator handling can lead to tls wildcard-depth authentication bypass due to resolver and verifier hostname normalization mismat](https://hackerone.com/reports/3688064)
   - Program: Node.js | Upvotes: 18 | Bounty: $0.00 | Type: Improper Handling of Unicode Encoding
90. [Uppercase sni context matching can lead to mtls authorization bypass due to case-sensitive hostname matching](https://hackerone.com/reports/3656869)
   - Program: Node.js | Upvotes: 7 | Bounty: $0.00 | Type: Improper Access Control - Generic
91. [TLS host identity verification bypass via session reuse with different servername leads to unauthorized connections](https://hackerone.com/reports/3649802)
   - Program: Node.js | Upvotes: 5 | Bounty: $0.00 | Type: Exploiting Incorrectly Configured SSL/TLS
92. [Permission Model bypass via FileHandle.utimes() in the promises API](https://hackerone.com/reports/3625987)
   - Program: Node.js | Upvotes: 4 | Bounty: $0.00 | Type: Incorrect Default Permissions
93. [Proxy credentials leaked in ERR_PROXY_TUNNEL error message](https://hackerone.com/reports/3720313)
   - Program: Node.js | Upvotes: 4 | Bounty: $0.00 | Type: Privacy Violation
94. [Unbounded memory growth in `node:http2` clients via attacker-controlled ORIGIN frames](https://hackerone.com/reports/3676863)
   - Program: Node.js | Upvotes: 4 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
95. [Embedded-nul hostnames can lead to silent authority rebinding due to c-string truncation in resolver bindings](https://hackerone.com/reports/3656716)
   - Program: Node.js | Upvotes: 4 | Bounty: $0.00 | Type: Improper Access Control - Generic
96. [Node.js WebCrypto AES Integer Overflow Leads to Remote Process Abort (DoS)](https://hackerone.com/reports/3760016)
   - Program: Node.js | Upvotes: 13 | Bounty: $0.00 | Type: Integer Overflow
97. [HTTPS proxy connection reuse lets one easy handle inherit another handle's mTLS-authenticated proxy session](https://hackerone.com/reports/3735180)
   - Program: curl | Upvotes: 6 | Bounty: $0.00 | Type: Exposure of Data Element to Wrong Session
98. [CVE-2026-11564: Native CA trust persist](https://hackerone.com/reports/3788984)
   - Program: curl | Upvotes: 7 | Bounty: $0.00 | Type: 
99. [CVE-2026-12064: proto-default skips SSH verification](https://hackerone.com/reports/3797526)
   - Program: curl | Upvotes: 8 | Bounty: $0.00 | Type: Improper Certificate Validation
100. [CVE-2026-11586: WS Auto-PONG memory exhaustion](https://hackerone.com/reports/3788931)
   - Program: curl | Upvotes: 6 | Bounty: $0.00 | Type: Allocation of Resources Without Limits or Throttling
101. [CVE-2026-11352: QUIC zero-length UDP datagrams busy-loop](https://hackerone.com/reports/3783438)
   - Program: curl | Upvotes: 7 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
102. [CVE-2026-10536: HTTP/2 stream-dependency tree UAF](https://hackerone.com/reports/3751697)
   - Program: curl | Upvotes: 5 | Bounty: $0.00 | Type: Buffer Over-read
103. [CVE-2026-8924: trailing dot domain super cookie](https://hackerone.com/reports/3733905)
   - Program: curl | Upvotes: 1 | Bounty: $0.00 | Type: Use of Incorrectly-Resolved Name or Reference
104. [CVE-2026-9547: SSH improper host validation](https://hackerone.com/reports/3751712)
   - Program: curl | Upvotes: 2 | Bounty: $0.00 | Type: Reusing a Nonce, Key Pair in Encryption
105. [CVE-2026-9546: sending old referer](https://hackerone.com/reports/3754343)
   - Program: curl | Upvotes: 3 | Bounty: $0.00 | Type: Use After Free
106. [CVE-2026-9079: stale proxy password leak](https://hackerone.com/reports/3750295)
   - Program: curl | Upvotes: 4 | Bounty: $0.00 | Type: Information Disclosure
107. [CVE-2026-9080: UAF after pause in socket callback](https://hackerone.com/reports/3749204)
   - Program: curl | Upvotes: 3 | Bounty: $0.00 | Type: Use After Free
108. [CVE-2026-8286: wrong STARTTLS connection reuse](https://hackerone.com/reports/3718195)
   - Program: curl | Upvotes: 2 | Bounty: $0.00 | Type: 
109. [CVE-2026-8932: incomplete mTLS config matching in conn reuse](https://hackerone.com/reports/3733910)
   - Program: curl | Upvotes: 3 | Bounty: $0.00 | Type: Business Logic Errors
110. [CVE-2026-8927: env-set cross-proxy Digest auth state leak](https://hackerone.com/reports/3744543)
   - Program: curl | Upvotes: 3 | Bounty: $0.00 | Type: Improper Authentication - Generic
111. [CVE-2026-8925: SASL double-free](https://hackerone.com/reports/3735193)
   - Program: curl | Upvotes: 2 | Bounty: $0.00 | Type: Double Free
112. [CVE-2026-8926: password leak with netrc and user in URL](https://hackerone.com/reports/3735184)
   - Program: curl | Upvotes: 2 | Bounty: $0.00 | Type: Information Disclosure
113. [CVE-2026-8458: wrong reuse for different services](https://hackerone.com/reports/3721183)
   - Program: curl | Upvotes: 2 | Bounty: $0.00 | Type: Authentication Bypass by Primary Weakness
114. [Insufficient checks in the file path parameter allow writing to unauthorized directories](https://hackerone.com/reports/3384615)
   - Program: SingleStore | Upvotes: 12 | Bounty: $0.00 | Type: External Control of File Name or Path
115. [CVE-2026-9545: exposing HTTP/3 early data](https://hackerone.com/reports/3752888)
   - Program: curl | Upvotes: 3 | Bounty: $0.00 | Type: Improper Certificate Validation
116. [CVE-2026-11856: cross-origin Digest auth state leak](https://hackerone.com/reports/3793260)
   - Program: curl | Upvotes: 2 | Bounty: $0.00 | Type: Information Exposure Through Sent Data
117. [Taskcluster web-server OAuth2 authorization codes are reusable and the exchange handler checks the wrong expiry column](https://hackerone.com/reports/3734676)
   - Program: Mozilla | Upvotes: 39 | Bounty: $2000.00 | Type: Authentication Bypass by Capture-replay
118. [Node --run POSIX positional argument escaping allows shell command injection](https://hackerone.com/reports/3817602)
   - Program: Node.js | Upvotes: 13 | Bounty: $0.00 | Type: OS Command Injection
119. [1-Click Account Takeover via Open Redirect through Regex Bypass in Domain Validation](https://hackerone.com/reports/3723458)
   - Program: Khan Academy | Upvotes: 115 | Bounty: $0.00 | Type: Improper Access Control - Generic
120. [HTTP/2 sessions never clean up after GOAWAY on invalid protocol errors](https://hackerone.com/reports/3658225)
   - Program: Node.js | Upvotes: 33 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
121. [Permission Model Bypass via `process.report.writeReport()` Path Misvalidation](https://hackerone.com/reports/3692858)
   - Program: Node.js | Upvotes: 29 | Bounty: $0.00 | Type: Improper Access Control - Generic
122. [Reflected XSS in AI Chat Bot Greetings at help.shopify.com via Markdown Image Rendering](https://hackerone.com/reports/2509022)
   - Program: Shopify | Upvotes: 96 | Bounty: $1600.00 | Type: Cross-site Scripting (XSS) - Reflected
123. [Authenticated Elasticsearch Painless script execution via Query.search.sort_query on hackerone.com/graphql](https://hackerone.com/reports/3694007)
   - Program: HackerOne | Upvotes: 155 | Bounty: $7000.00 | Type: Code Injection
124. [verify-release rebuilds from the tarball under verification, enabling pre-check command execution and false OK for a malicious curl release tarball](https://hackerone.com/reports/3802645)
   - Program: curl | Upvotes: 14 | Bounty: $0.00 | Type: Reliance on Untrusted Inputs in a Security Decision
125. [Vulnerability Report: Buffer Overflow in Path Sanitization](https://hackerone.com/reports/3804525)
   - Program: curl | Upvotes: 30 | Bounty: $0.00 | Type: 
126. [Unauthenticated file deletion via deleteFileMessage DDP method allows permanent destruction of any uploaded file](https://hackerone.com/reports/3611837)
   - Program: Rocket.Chat | Upvotes: 33 | Bounty: $0.00 | Type: Improper Authentication - Generic
127. [Malicious Conflux Endpoint Can Leave Stale Global OOO Queue Accounting After Teardown](https://hackerone.com/reports/3701692)
   - Program: Tor | Upvotes: 34 | Bounty: $100.00 | Type: Uncontrolled Resource Consumption
128. [Unauthenticated reading of every file via livechat auth and predicting MongoDB ObjectId()](https://hackerone.com/reports/3687142)
   - Program: Rocket.Chat | Upvotes: 45 | Bounty: $0.00 | Type: Improper Access Control - Generic
129. [Reflected Cross-Site Scripting (XSS) found on IBM.com domain](https://hackerone.com/reports/3664261)
   - Program: IBM | Upvotes: 29 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
130. [Incomplete Suppression of  Transfer-Encoding: chunked Header in HTTP/2 After Redirect From HTTP/1.1](https://hackerone.com/reports/3793495)
   - Program: curl | Upvotes: 21 | Bounty: $0.00 | Type: HTTP Request Smuggling
131. [Secure cookies leaked to HTTP origins through HTTPS forwarding proxy](https://hackerone.com/reports/3803415)
   - Program: curl | Upvotes: 14 | Bounty: $0.00 | Type: Information Disclosure
132. [UI Consent Bypass via Comma Injection in `addAutoApproveTarget` — User-Approval Dialog and Persistence Layer Disagree on Target Scope, Yielding Authen](https://hackerone.com/reports/3717354)
   - Program: PortSwigger Web Security | Upvotes: 27 | Bounty: $0.00 | Type: LLM09:2025 Misinformation
133. [Burp Suite Professional: browser-powered crawl can write attacker-controlled files through file input handling](https://hackerone.com/reports/3712279)
   - Program: PortSwigger Web Security | Upvotes: 160 | Bounty: $5000.00 | Type: Path Traversal
134. [Duplicate chunked Transfer-Encoding lets a malicious origin smuggle a response across reused HTTP proxy connections](https://hackerone.com/reports/3795615)
   - Program: curl | Upvotes: 18 | Bounty: $0.00 | Type: HTTP Request Smuggling
135. [Incomplete Fix for CVE-2026-21637: OCSPRequest and resumeSession Events Crash Node.js TLS Server via Unhandled Synchronous Exceptions](https://hackerone.com/reports/3781015)
   - Program: Node.js | Upvotes: 41 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
136. [Command Injection via Unsanitized Bundling Options in `aws-cdk-lib/aws-lambda-nodejs`](https://hackerone.com/reports/3558713)
   - Program: AWS VDP | Upvotes: 48 | Bounty: $0.00 | Type: OS Command Injection
137. [Firecracker Out-of-bounds Read/Write Local Privilege Escalation Vulnerability](https://hackerone.com/reports/3738654)
   - Program: AWS VDP | Upvotes: 33 | Bounty: $0.00 | Type: Out-of-bounds Read
138. [CRLF Injection via Custom HTTP Headers](https://hackerone.com/reports/3741744)
   - Program: curl | Upvotes: 20 | Bounty: $0.00 | Type: CRLF Injection
139. [heap-use-after-free in state.referer when CURLOPT_REFERER replaced or cleared after perform](https://hackerone.com/reports/3774279)
   - Program: curl | Upvotes: 22 | Bounty: $0.00 | Type: Use After Free
140. [RCE + PAT Exfiltration via pull_request_target in privacy-configuration/auto-respond-pr.yml — Direct Supply Chain to All DDG Browsers](https://hackerone.com/reports/3619288)
   - Program: DuckDuckGo | Upvotes: 63 | Bounty: $0.00 | Type: 
141. [RCE + Supply Chain Attack via pull_request_target in content-scope-scripts/semver-label.yml — Affects All DuckDuckGo Browsers](https://hackerone.com/reports/3619287)
   - Program: DuckDuckGo | Upvotes: 40 | Bounty: $0.00 | Type: 
142. [SSRF via Improper Redirect Validation in Rocket.Chat oEmbed Function](https://hackerone.com/reports/3383079)
   - Program: Rocket.Chat | Upvotes: 24 | Bounty: $0.00 | Type: Server-Side Request Forgery (SSRF)
143. [SSRF via improper validation after DNS name resolution in the link-preview feature](https://hackerone.com/reports/3393664)
   - Program: Rocket.Chat | Upvotes: 24 | Bounty: $0.00 | Type: Server-Side Request Forgery (SSRF)
144. [curl-ipv4-percent-normalization-SSRF](https://hackerone.com/reports/3791168)
   - Program: curl | Upvotes: 12 | Bounty: $0.00 | Type: Server-Side Request Forgery (SSRF)
145. [Trailing-Dot Hostname in Redirect Silently Strips Client Certificate and Auth Credentials](https://hackerone.com/reports/3791191)
   - Program: curl | Upvotes: 11 | Bounty: $0.00 | Type: Improper Authentication - Generic
146. [curl/libcurl vulnerable to TLS truncation attacks](https://hackerone.com/reports/1826392)
   - Program: curl | Upvotes: 7 | Bounty: $0.00 | Type: Business Logic Errors
147. [SSH/SFTP connection reuse can bypass SSH key identity after ssh_config_matches removal](https://hackerone.com/reports/3788506)
   - Program: curl | Upvotes: 28 | Bounty: $0.00 | Type: Authentication Bypass by Primary Weakness
148. [SOCKS5 no-auth accepted despite username/password-only authentication](https://hackerone.com/reports/3786077)
   - Program: curl | Upvotes: 10 | Bounty: $0.00 | Type: Improper Authentication - Generic
149. [Action Text ReDoS (Ruby 3.1  or lower)](https://hackerone.com/reports/2389431)
   - Program: Ruby on Rails | Upvotes: 28 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
150. [libcurl: HTTP/1.x bare LF byte in response header value enables cookie jar pollution and POST body/credential exfiltration via redirect — RC=0, curl 8](https://hackerone.com/reports/3785919)
   - Program: curl | Upvotes: 18 | Bounty: $0.00 | Type: HTTP Response Splitting
151. [DNS domain search list followed for extant domain missing A or AAAA records](https://hackerone.com/reports/3780733)
   - Program: curl | Upvotes: 12 | Bounty: $0.00 | Type: Use of Incorrectly-Resolved Name or Reference
152. [OpenSSL TLS 1.2 session resumption accepts expired server certificates in libcurl](https://hackerone.com/reports/3781305)
   - Program: curl | Upvotes: 14 | Bounty: $0.00 | Type: Improper Validation of Certificate Expiration
153. [curl cross-origin HTTPS redirect reuses TLS client certificate for unintended second-origin mTLS authentication](https://hackerone.com/reports/3749428)
   - Program: curl | Upvotes: 11 | Bounty: $0.00 | Type: Insufficiently Protected Credentials
154. [curl External-Controlled Filename in `--url @file` Leads to Arbitrary File Overwrite](https://hackerone.com/reports/3766392)
   - Program: curl | Upvotes: 13 | Bounty: $0.00 | Type: External Control of File Name or Path
155. [Valid share tokens allow to access tempory upload files of share owner](https://hackerone.com/reports/3483708)
   - Program: Nextcloud | Upvotes: 26 | Bounty: $0.00 | Type: Improper Access Control - Generic
156. [Authentication Bypass in ID4me handling via Missing JWT Signature Verification in User OIDC](https://hackerone.com/reports/3489490)
   - Program: Nextcloud | Upvotes: 51 | Bounty: $2500.00 | Type: Improper Authentication - Generic
157. [PIN bypass in PassCodeActivity via back button](https://hackerone.com/reports/3625210)
   - Program: Nextcloud | Upvotes: 14 | Bounty: $0.00 | Type: Improper Authentication - Generic
158. [GnuTLS OCSP stapling accepts unrelated SingleResponse (no cert-ID binding)](https://hackerone.com/reports/3784125)
   - Program: curl | Upvotes: 23 | Bounty: $0.00 | Type: Improper Certificate Validation
159. [DLL side-loading vulnerability in Sony Music Center for PC Ver. 2.7.2 (Latest version)](https://hackerone.com/reports/3355766)
   - Program: Sony | Upvotes: 109 | Bounty: $0.00 | Type: Uncontrolled Search Path Element
160. [CURLOPT_PROXY_CRLFILE / CURLOPT_PROXY_ISSUERCERT / CURLOPT_PROXY_ISSUERCERT_BLOB silently ignored on backends that don't support them](https://hackerone.com/reports/3717552)
   - Program: curl | Upvotes: 13 | Bounty: $0.00 | Type: Improper Check for Certificate Revocation
161. [Shared HSTS cache accessed without lock](https://hackerone.com/reports/3718265)
   - Program: curl | Upvotes: 13 | Bounty: $0.00 | Type: 
162. [RTSP Digest auth state leaks across origins on reused libcurl easy handle](https://hackerone.com/reports/3776535)
   - Program: curl | Upvotes: 10 | Bounty: $0.00 | Type: Information Exposure Through Sent Data
163. [TFTP upload ignores --continue-at / CURLOPT_RESUME_FROM and leaks skipped local file prefix](https://hackerone.com/reports/3776433)
   - Program: curl | Upvotes: 8 | Bounty: $0.00 | Type: Information Exposure Through Sent Data
164. [libcurl 8.20.0 ignores HTTP Digest domain protection space and preemptively leaks Digest auth outside the declared scope](https://hackerone.com/reports/3774977)
   - Program: curl | Upvotes: 6 | Bounty: $0.00 | Type: 
165. [CURLOPT_COOKIE leaked to cross-origin redirect target — CURLOPT_UNRESTRICTED_AUTH bypass for the STRING_COOKIE path](https://hackerone.com/reports/3766065)
   - Program: curl | Upvotes: 4 | Bounty: $0.00 | Type: Information Disclosure
166. [Missing access control when linking banners or campaigns to zones](https://hackerone.com/reports/3650504)
   - Program: Revive Adserver | Upvotes: 42 | Bounty: $0.00 | Type: Improper Access Control - Generic
167. [Missing access control when linking trackers to campaigns](https://hackerone.com/reports/3650582)
   - Program: Revive Adserver | Upvotes: 34 | Bounty: $0.00 | Type: Improper Access Control - Generic
168. [Blind SQL injection via clientid parameter in zone‑include.php](https://hackerone.com/reports/3653196)
   - Program: Revive Adserver | Upvotes: 47 | Bounty: $0.00 | Type: SQL Injection
169. [Reflected XSS via clientid parameter in zone‑include.php](https://hackerone.com/reports/3653316)
   - Program: Revive Adserver | Upvotes: 24 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
170. [PHP code injection via delivery limitation logical](https://hackerone.com/reports/3656781)
   - Program: Revive Adserver | Upvotes: 35 | Bounty: $0.00 | Type: Code Injection
171. [Stored XSS via Full Name field in userlog email entries](https://hackerone.com/reports/3669623)
   - Program: Revive Adserver | Upvotes: 20 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Stored
172. [Session ID reuse allowing XML‑RPC API authentication bypass](https://hackerone.com/reports/3672641)
   - Program: Revive Adserver | Upvotes: 6 | Bounty: $0.00 | Type: Improper Authentication - Generic
173. [Missing access control when modifying parent entities via XML‑RPC](https://hackerone.com/reports/3677576)
   - Program: Revive Adserver | Upvotes: 6 | Bounty: $0.00 | Type: Improper Access Control - Generic
174. [Banner status override by advertiser‑level users](https://hackerone.com/reports/3678828)
   - Program: Revive Adserver | Upvotes: 3 | Bounty: $0.00 | Type: Improper Access Control - Generic
175. [Stored XSS via malicious usernames in audit log details + Username validation bypass in XML‑RPC addUser](https://hackerone.com/reports/3680090)
   - Program: Revive Adserver | Upvotes: 7 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Stored
176. [PHP code injection via unexpected delivery limitation parameter](https://hackerone.com/reports/3744200)
   - Program: Revive Adserver | Upvotes: 10 | Bounty: $0.00 | Type: Code Injection
177. [PRE_PROXY change leaks stale Proxy Digest state across proxy-chain boundary](https://hackerone.com/reports/3777381)
   - Program: curl | Upvotes: 1 | Bounty: $0.00 | Type: Information Disclosure
178. [curl/libcurl 8.20.0 NOPROXY bypass via uppercase-hex IPv4 aliases leaks off-proxy Basic credentials to the configured proxy](https://hackerone.com/reports/3773293)
   - Program: curl | Upvotes: 2 | Bounty: $0.00 | Type: 
179. [SMTP connection reuse ignores --ssl-reqd / CURLOPT_USE_SSL and reuses a clear-text STARTTLS session on current master](https://hackerone.com/reports/3770979)
   - Program: curl | Upvotes: 1 | Bounty: $0.00 | Type: Cleartext Transmission of Sensitive Information
180. [Proxy CONNECT response poisoning via authentication retry in cf-h1-proxy.c (libcurl)](https://hackerone.com/reports/3767963)
   - Program: curl | Upvotes: 2 | Bounty: $0.00 | Type: Business Logic Errors
181. [Incomplete fix for CVE-2022-35406: meta-redirect content-type check bypassable via parameter injection](https://hackerone.com/reports/3775183)
   - Program: PortSwigger Web Security | Upvotes: 18 | Bounty: $0.00 | Type: Open Redirect
182. [page.line.me Open Redirect Leading to OAuth Authorization Code Exposure and Access Token Compromise](https://hackerone.com/reports/3423013)
   - Program: LY Corporation | Upvotes: 43 | Bounty: $1000.00 | Type: 
183. [Missing HMAC validation on /uninstall webhook in Shopify/sample-django-app reference template](https://hackerone.com/reports/3697491)
   - Program: Shopify | Upvotes: 18 | Bounty: $0.00 | Type: Improper Verification of Cryptographic Signature
184. [Mentioned unites are at the same time .Then we have to increase the bounty.](https://hackerone.com/reports/3761789)
   - Program: curl | Upvotes: 17 | Bounty: $0.00 | Type: Forced Browsing
185. [TLS conn reuse and session cache ignore fsslctx callback and ssl_config_data flags ( incomplete fix variant of 7541ae569 )](https://hackerone.com/reports/3761647)
   - Program: curl | Upvotes: 16 | Bounty: $0.00 | Type: Insufficiently Protected Credentials
186. [lib/ldap.c follows attacker-controlled LDAP referrals and binds to a second server; WinLDAP builds leak current logon credentials (confirmed on Window](https://hackerone.com/reports/3756699)
   - Program: curl | Upvotes: 8 | Bounty: $0.00 | Type: Insufficiently Protected Credentials
187. [Use-after-free in `curl_easy_duphandle()` with HTTP/2 stream-dependency tree](https://hackerone.com/reports/3751701)
   - Program: curl | Upvotes: 5 | Bounty: $0.00 | Type: Use After Free
188. [Low priority HSTS bypass in curl_easy_duphandle()](https://hackerone.com/reports/3769293)
   - Program: curl | Upvotes: 5 | Bounty: $0.00 | Type: Information Exposure Through Sent Data
189. [Blind POST SSRF via Web Push Notification Endpoint](https://hackerone.com/reports/3608558)
   - Program: phpBB | Upvotes: 31 | Bounty: $0.00 | Type: Server-Side Request Forgery (SSRF)
190. [V1Plugin.Decrypt panics on empty ciphertext (Remote DoS)](https://hackerone.com/reports/3620748)
   - Program: AWS VDP | Upvotes: 41 | Bounty: $0.00 | Type: Array Index Underflow
191. [V2Plugin.Decrypt panics on empty ciphertext (Remote DoS)](https://hackerone.com/reports/3620753)
   - Program: AWS VDP | Upvotes: 25 | Bounty: $0.00 | Type: Array Index Underflow
192. [iOS Brave Playlist "Open in Private Tab" bypasses FaceID requirement for Private Tabs](https://hackerone.com/reports/3693295)
   - Program: Brave Software | Upvotes: 48 | Bounty: $0.00 | Type: Improper Authentication - Generic
193. [Heap-OOB read in urlapi `redirect_url()` via `CURLU_GUESS_SCHEME` + `CURLU_NO_GUESS_SCHEME` flow](https://hackerone.com/reports/3751715)
   - Program: curl | Upvotes: 27 | Bounty: $0.00 | Type: Buffer Over-read
194. [curl GnuTLS backend accepts a clientAuth-only certificate for HTTPS server authentication](https://hackerone.com/reports/3752567)
   - Program: curl | Upvotes: 24 | Bounty: $0.00 | Type: Improper Certificate Validation
195. [Autotranslate DDP Method Exposes Private Messages Without Authentication or Room Access Check](https://hackerone.com/reports/3734326)
   - Program: Rocket.Chat | Upvotes: 70 | Bounty: $0.00 | Type: Insecure Direct Object Reference (IDOR)
196. [NULL pointer dereference in node:sqlite DatabaseSync#applyChangeset() via malformed SQLite changeset](https://hackerone.com/reports/3736889)
   - Program: Node.js | Upvotes: 44 | Bounty: $0.00 | Type: NULL Pointer Dereference
197. [Memory Corruption via TOCTOU Race in SharedArrayBuffer UTF-8 Decode (`StringBytes::Encode`)](https://hackerone.com/reports/3752489)
   - Program: Node.js | Upvotes: 31 | Bounty: $0.00 | Type: Time-of-check Time-of-use (TOCTOU) Race Condition
198. [Group restriction bypass via bearer token in user_oidc (SETTING_RESTRICT_LOGIN_TO_GROUPS not enforced in Backend::getCurrentUserId)](https://hackerone.com/reports/3572848)
   - Program: Nextcloud | Upvotes: 68 | Bounty: $0.00 | Type: Improper Access Control - Generic
199. [curl --skip-existing has a TOCTOU race that lets a post-check symlink redirect the later download write](https://hackerone.com/reports/3747959)
   - Program: curl | Upvotes: 42 | Bounty: $0.00 | Type: Time-of-check Time-of-use (TOCTOU) Race Condition
200. [Credentials forwarded to HTTP after HTTPS→HTTP same-port redirect — url_set_data_creds uses scheme-blind comparator](https://hackerone.com/reports/3733946)
   - Program: curl | Upvotes: 35 | Bounty: $0.00 | Type: 
