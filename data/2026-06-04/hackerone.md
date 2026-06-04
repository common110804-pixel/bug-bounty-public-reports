# HackerOne Public Reports Snapshot

Generated: 2026-06-04T16:33:40.546236+00:00

1. [NULL pointer dereference in node:sqlite DatabaseSync#applyChangeset() via malformed SQLite changeset](https://hackerone.com/reports/3736889)
   - Program: Node.js | Upvotes: 7 | Bounty: $0.00 | Type: NULL Pointer Dereference
2. [Memory Corruption via TOCTOU Race in SharedArrayBuffer UTF-8 Decode (`StringBytes::Encode`)](https://hackerone.com/reports/3752489)
   - Program: Node.js | Upvotes: 6 | Bounty: $0.00 | Type: Time-of-check Time-of-use (TOCTOU) Race Condition
3. [Group restriction bypass via bearer token in user_oidc (SETTING_RESTRICT_LOGIN_TO_GROUPS not enforced in Backend::getCurrentUserId)](https://hackerone.com/reports/3572848)
   - Program: Nextcloud | Upvotes: 31 | Bounty: $0.00 | Type: Improper Access Control - Generic
4. [curl --skip-existing has a TOCTOU race that lets a post-check symlink redirect the later download write](https://hackerone.com/reports/3747959)
   - Program: curl | Upvotes: 20 | Bounty: $0.00 | Type: Time-of-check Time-of-use (TOCTOU) Race Condition
5. [Credentials forwarded to HTTP after HTTPS→HTTP same-port redirect — url_set_data_creds uses scheme-blind comparator](https://hackerone.com/reports/3733946)
   - Program: curl | Upvotes: 17 | Bounty: $0.00 | Type: 
6. [POST /api/bitcoinWithdrawalFees returns financial data without authentication despite being documented as a USER OPERATION (private endpoint)](https://hackerone.com/reports/3676308)
   - Program: CoinMate.io | Upvotes: 48 | Bounty: $0.00 | Type: Improper Authentication - Generic
7. [HMAC signature verification omits endpoint and payload allowing request forgery on CoinMate API](https://hackerone.com/reports/3670955)
   - Program: CoinMate.io | Upvotes: 40 | Bounty: $0.00 | Type: Missing Required Cryptographic Step
8. [HTTP/3 paused transfer buffers incoming data without bound up to ~1 GiB](https://hackerone.com/reports/3734947)
   - Program: curl | Upvotes: 26 | Bounty: $0.00 | Type: Allocation of Resources Without Limits or Throttling
9. [Schannel custom-CA path skips Extended Key Usage enforcement](https://hackerone.com/reports/3734992)
   - Program: curl | Upvotes: 20 | Bounty: $0.00 | Type: Business Logic Errors
10. [Connection reuse ignores haproxyprotocol and HAPROXY_CLIENT_IP settings, allowing PROXY context to persist across transfers](https://hackerone.com/reports/3741135)
   - Program: curl | Upvotes: 15 | Bounty: $0.00 | Type: Incorrect Authorization
11. [SSL session-cache peer key omits signature_algorithms: strict-sigalg handle silently resumes a permissive sibling's session](https://hackerone.com/reports/3739561)
   - Program: curl | Upvotes: 13 | Bounty: $0.00 | Type: Improper Certificate Validation
12. [CURLOPT_PROXY_CAINFO_BLOB silently activates native CA store on Apple builds](https://hackerone.com/reports/3735179)
   - Program: curl | Upvotes: 12 | Bounty: $0.00 | Type: Business Logic Errors
13. [TLS peer-verification bypass via mid-transfer ssl_config mutation](https://hackerone.com/reports/3735276)
   - Program: curl | Upvotes: 8 | Bounty: $0.00 | Type: Business Logic Errors
14. [TLS verifyhost bypass in rustls, mbedTLS, and wolfSSL when verifypeer=0](https://hackerone.com/reports/3734095)
   - Program: curl | Upvotes: 4 | Bounty: $0.00 | Type: Business Logic Errors
15. [HTTP/2 proxy CONNECT tunnel unbounded 1xx chain (missing Curl_bump_headersize cap in cf-h2-proxy.c)](https://hackerone.com/reports/3734020)
   - Program: curl | Upvotes: 4 | Bounty: $0.00 | Type: Allocation of Resources Without Limits or Throttling
16. [Cross-repository IDOR in `/settings/security_analysis/bypass_reviewers` allows unauthorized delegated bypass reviewer modification](https://hackerone.com/reports/3560256)
   - Program: GitHub | Upvotes: 50 | Bounty: $0.00 | Type: Insecure Direct Object Reference (IDOR)
17. [CURLOPT_HSTS_CTRL disables shared HSTS without share guard — use-after-free and double-free](https://hackerone.com/reports/3733934)
   - Program: curl | Upvotes: 10 | Bounty: $0.00 | Type: Use After Free
18. [cookie: case-insensitive path comparison in replace_existing() allows cookie eviction across distinct paths](https://hackerone.com/reports/3735238)
   - Program: curl | Upvotes: 9 | Bounty: $0.00 | Type: Business Logic Errors
19. [libssh SFTP initialization ignores CURLOPT_TIMEOUT, hangs indefinitely](https://hackerone.com/reports/3735080)
   - Program: curl | Upvotes: 9 | Bounty: $0.00 | Type: Allocation of Resources Without Limits or Throttling
20. [rustls backend silently ignores CURLOPT_CRLFILE when native CA store is active](https://hackerone.com/reports/3734935)
   - Program: curl | Upvotes: 8 | Bounty: $0.00 | Type: Business Logic Errors
21. [HSTS multi-trailing-dot bypass-ish: possible incomplete fix for CVE-2022-30115](https://hackerone.com/reports/3733984)
   - Program: curl | Upvotes: 8 | Bounty: $0.00 | Type: Cleartext Transmission of Sensitive Information
22. [Unauthenticated File Upload to CDN](https://hackerone.com/reports/3589247)
   - Program: Enjin | Upvotes: 37 | Bounty: $0.00 | Type: Improper Access Control - Generic
23. [IDOR: autotranslate.translateMessage Full Message Content Leak](https://hackerone.com/reports/3713682)
   - Program: Rocket.Chat | Upvotes: 30 | Bounty: $0.00 | Type: Insecure Direct Object Reference (IDOR)
24. [Trailing-dot IPv4 URL bypasses IP-address guard, allows wildcard DNS SAN match](https://hackerone.com/reports/3734921)
   - Program: curl | Upvotes: 8 | Bounty: $0.00 | Type: Business Logic Errors
25. [NULL pointer dereference in libcurl URL API redirect_url() with CURLU_DEFAULT_SCHEME](https://hackerone.com/reports/3736234)
   - Program: curl | Upvotes: 4 | Bounty: $0.00 | Type: NULL Pointer Dereference
26. [SQL Injection in Column Type Parameter Allows Arbitrary SQL Execution](https://hackerone.com/reports/3462991)
   - Program: Nextcloud | Upvotes: 70 | Bounty: $0.00 | Type: SQL Injection
27. [Kerberos/SPNEGO Connection Reuse Vulnerability](https://hackerone.com/reports/3725659)
   - Program: curl | Upvotes: 21 | Bounty: $0.00 | Type: 
28. [QuickSight Authorization Bypass: Chat Agents Accessible Despite Custom Permissions Denial](https://hackerone.com/reports/3577145)
   - Program: AWS VDP | Upvotes: 57 | Bounty: $0.00 | Type: 
29. [another liberapay member team twitter account broken Link Hijacking via Expired Twitter Account Link](https://hackerone.com/reports/3723002)
   - Program: Liberapay | Upvotes: 76 | Bounty: $0.00 | Type: Open Redirect
30. [Liberapay member team twitter account broken Link Hijacking via Expired Twitter Account Link](https://hackerone.com/reports/3721519)
   - Program: Liberapay | Upvotes: 62 | Bounty: $0.00 | Type: Open Redirect
31. [Private circle can be added to another circle via API despite visibility restriction](https://hackerone.com/reports/3511998)
   - Program: Nextcloud | Upvotes: 76 | Bounty: $150.00 | Type: Insecure Direct Object Reference (IDOR)
32. [Files drop share links for end-to-end encrypted folders allowed to drop files into other folders of the share owner](https://hackerone.com/reports/3304830)
   - Program: Nextcloud | Upvotes: 56 | Bounty: $0.00 | Type: Insecure Direct Object Reference (IDOR)
33. [View-only guests could see deleted Collectives pages in the trashbin](https://hackerone.com/reports/3521434)
   - Program: Nextcloud | Upvotes: 58 | Bounty: $0.00 | Type: Improper Access Control - Generic
34. [mbedTLS private-key blob null-termination asymmetry in lib/vtls/mbedtls.c (mbed_load_privkey)](https://hackerone.com/reports/3717365)
   - Program: curl | Upvotes: 41 | Bounty: $0.00 | Type: Improper Null Termination
35. [ActiveStorage Disk Service Path Traversal via Custom Blob Key Injection](https://hackerone.com/reports/3580511)
   - Program: Ruby on Rails | Upvotes: 53 | Bounty: $0.00 | Type: Path Traversal
36. [Critical Deadlock Vulnerability in Monero RPC Leading to Complete Node Paralysis](https://hackerone.com/reports/3307874)
   - Program: Monero | Upvotes: 81 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
37. [Connection Count Bug in Monero Node Enables Outbound Peer Reset Attack](https://hackerone.com/reports/3185083)
   - Program: Monero | Upvotes: 38 | Bounty: $0.00 | Type: Privacy Violation
38. [wcurl treats some URL operands after -- as curl options](https://hackerone.com/reports/3708482)
   - Program: curl | Upvotes: 23 | Bounty: $0.00 | Type: Improper Neutralization of Value Delimiters
39. [Out of scope: Improper Input Validation Order on /api-internal/login via password field leads to unnecessary resource consumption](https://hackerone.com/reports/3625600)
   - Program: PortSwigger Web Security | Upvotes: 77 | Bounty: $200.00 | Type: 
40. [Potential Resource Leak in tool_parsecfg.c at line 279 during fileerror](https://hackerone.com/reports/3710209)
   - Program: curl | Upvotes: 21 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
41. [libcurl 8.20.0 incomplete fix for CVE-2026-7168: changing only CURLOPT_PROXYPORT leaks stale Proxy Digest auth to a different proxy](https://hackerone.com/reports/3707747)
   - Program: curl | Upvotes: 18 | Bounty: $0.00 | Type: 
42. [MQTT CONNACK Packet Type Bypass leads to RCE via Malicious Broker](https://hackerone.com/reports/3712343)
   - Program: curl | Upvotes: 28 | Bounty: $0.00 | Type: ASI05: Unexpected Code Execution (RCE)
43. [Improper input validation On Exported deep-link handler crashes `FileDisplayActivity` on crafted external URL — Denial-of-Service](https://hackerone.com/reports/3399016)
   - Program: Nextcloud | Upvotes: 63 | Bounty: $0.00 | Type: Improper Null Termination
44. [Double fdrop on a socket through sys_netcontrol](https://hackerone.com/reports/3320669)
   - Program: PlayStation | Upvotes: 184 | Bounty: $10000.00 | Type: Double Free
45. [MQTT state machine confusion: PINGRESP/DISCONNECT with non-zero remaining_length dispatches to stale nextstate](https://hackerone.com/reports/3702718)
   - Program: curl | Upvotes: 36 | Bounty: $0.00 | Type: Improper Input Validation
46. [Use-After-Free in SMB connection reuse (req->path dangling pointer after needle destruction)](https://hackerone.com/reports/3591956)
   - Program: curl | Upvotes: 57 | Bounty: $0.00 | Type: Use After Free
47. [Negotiate connection reuse with wrong credentials when using CURLAUTH_ANY](https://hackerone.com/reports/3646072)
   - Program: curl | Upvotes: 45 | Bounty: $0.00 | Type: Authentication Bypass by Primary Weakness
48. [Negotiate Authentication Premature on Connection Reuse](https://hackerone.com/reports/3666576)
   - Program: curl | Upvotes: 38 | Bounty: $0.00 | Type: Improper Authentication - Generic
49. [CVE-2026-7168: cross-proxy Digest auth state leak](https://hackerone.com/reports/3697719)
   - Program: curl | Upvotes: 37 | Bounty: $0.00 | Type: Exposure of Data Element to Wrong Session
50. [CVE-2026-7009: OCSP stapling bypass with Apple SecTrust](https://hackerone.com/reports/3694390)
   - Program: curl | Upvotes: 33 | Bounty: $0.00 | Type: Improper Certificate Validation
51. [CVE-2026-6253: proxy credentials leak over redirect-to proxy](https://hackerone.com/reports/3669637)
   - Program: curl | Upvotes: 24 | Bounty: $0.00 | Type: 
52. [CVE-2026-5545: wrong reuse of HTTP Negotiate connection](https://hackerone.com/reports/3642555)
   - Program: curl | Upvotes: 22 | Bounty: $0.00 | Type: Authentication Bypass by Primary Weakness
53. [CVE-2026-6276: stale custom cookie host causes cookie leak](https://hackerone.com/reports/3671818)
   - Program: curl | Upvotes: 24 | Bounty: $0.00 | Type: Exposure of Data Element to Wrong Session
54. [CVE-2026-6429: netrc credential leak with reused proxy connection](https://hackerone.com/reports/3677759)
   - Program: curl | Upvotes: 19 | Bounty: $0.00 | Type: Information Exposure Through Sent Data
55. [CVE-2026-4873: connection reuse ignores TLS requirement](https://hackerone.com/reports/3621851)
   - Program: curl | Upvotes: 13 | Bounty: $0.00 | Type: Cleartext Transmission of Sensitive Information
56. [CVE-2026-5773: wrong reuse of SMB connection](https://hackerone.com/reports/3650689)
   - Program: curl | Upvotes: 11 | Bounty: $0.00 | Type: 
57. [Use-after-free in `curl_easy_ssls_export()` during callback re-entrancy](https://hackerone.com/reports/3682666)
   - Program: curl | Upvotes: 8 | Bounty: $0.00 | Type: Use After Free
58. [Heap-buffer-overflow in `Curl_ssl_push_certinfo_len()` — sole bounds check is `DEBUGASSERT`](https://hackerone.com/reports/3684614)
   - Program: curl | Upvotes: 7 | Bounty: $0.00 | Type: Out-of-bounds Read
59. [Stack exhaustion in MIME multipart reading with deeply nested subparts](https://hackerone.com/reports/3684603)
   - Program: curl | Upvotes: 4 | Bounty: $0.00 | Type: Uncontrolled Recursion
60. [PS4 BD-J privilege escalation using nested JAR](https://hackerone.com/reports/3452696)
   - Program: PlayStation | Upvotes: 71 | Bounty: $2500.00 | Type: Privilege Escalation
61. [IBM Aspera HTTP Gateway stores sensitive information in clear text in easily obtainable files which can be read by an unauthenticated user.](https://hackerone.com/reports/3340797)
   - Program: IBM | Upvotes: 44 | Bounty: $0.00 | Type: Information Disclosure
62. [Bypass of Restricted Keyword "Mozilla" in Display Name Field via Unicode Homoglyphs on addons.allizom.org](https://hackerone.com/reports/3279441)
   - Program: Mozilla | Upvotes: 81 | Bounty: $500.00 | Type: Improper Input Validation
63. [Bypassing Inbox Privacy Settings and Enabling Spam on Pixiv.net](https://hackerone.com/reports/3100570)
   - Program: pixiv | Upvotes: 46 | Bounty: $200.00 | Type: Improper Access Control - Generic
64. [Non-premium user can disable Ads in japanese version of dic.pixiv.net](https://hackerone.com/reports/3183520)
   - Program: pixiv | Upvotes: 104 | Bounty: $3000.00 | Type: Business Logic Errors
65. [Argument Injection in /manage/ssh/ via host parameter leads to sensitive file disclosure on Weblate](https://hackerone.com/reports/3518571)
   - Program: Weblate | Upvotes: 32 | Bounty: $0.00 | Type: 
66. [mruby-engine: UAF in MRubyEngine#initialize enables local RCE](https://hackerone.com/reports/3679660)
   - Program: Shopify | Upvotes: 32 | Bounty: $0.00 | Type: 
67. [Incomplete fix for CVE-2026-21637: loadSNI() in _tls_wrap.js lacks try/catch leading to Remote DoS](https://hackerone.com/reports/3556769)
   - Program: Node.js | Upvotes: 57 | Bounty: $0.00 | Type: 
68. [RBAC bypass on App log endpoints via `permissionRequired` typo — any authenticated user reads admin-only Enterprise App logs](https://hackerone.com/reports/3589551)
   - Program: Rocket.Chat | Upvotes: 39 | Bounty: $0.00 | Type: Improper Access Control - Generic
69. [Complete authentication bypass to admin permissions](https://hackerone.com/reports/3564655)
   - Program: Rocket.Chat | Upvotes: 89 | Bounty: $0.00 | Type: SQL Injection
70. [SVG filter primitives bypass remote image blocking, enabling email tracking without consent.](https://hackerone.com/reports/3486747)
   - Program: Nextcloud | Upvotes: 53 | Bounty: $0.00 | Type: Privacy Violation
71. [position: fixed !important bypasses CSS sanitizer's fixed-position mitigation, enabling full-viewport phishing overlays.](https://hackerone.com/reports/3590586)
   - Program: Nextcloud | Upvotes: 43 | Bounty: $0.00 | Type: Resource Injection
72. [Unquoted body background attribute enables CSS injection that bypasses remote image blocking](https://hackerone.com/reports/3590583)
   - Program: Nextcloud | Upvotes: 33 | Bounty: $0.00 | Type: Resource Injection
73. [SMIL values and by attributes bypass remote image blocking via unvalidated resource-loading animations, enabling email tracking without consent](https://hackerone.com/reports/3590576)
   - Program: Nextcloud | Upvotes: 26 | Bounty: $0.00 | Type: Remote File Inclusion
74. [libcurl omits IPv6 zoneid from host identity and leaks credentials/cookies across scoped link-local realms](https://hackerone.com/reports/3680680)
   - Program: curl | Upvotes: 29 | Bounty: $0.00 | Type: Information Disclosure
75. [Digest Auth State Leak on Cross-Origin Redirect via Netrc - Username and Password Hash Sent to Wrong Host](https://hackerone.com/reports/3680038)
   - Program: curl | Upvotes: 17 | Bounty: $0.00 | Type: Insufficiently Protected Credentials
76. [Stored XSS in attachment-display exploitable through SameSite](https://hackerone.com/reports/3594137)
   - Program: Nextcloud | Upvotes: 36 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Stored
77. [libcurl reuses a learned RTSP Session header across different hosts on the same easy handle, enabling cross-host session leak and replay](https://hackerone.com/reports/3680234)
   - Program: curl | Upvotes: 13 | Bounty: $0.00 | Type: Exposure of Data Element to Wrong Session
78. [Rails::HTML::Sanitizer.allowed_uri? returns true for entity-encoded control-character-split javascript: URLs](https://hackerone.com/reports/3601655)
   - Program: Ruby on Rails | Upvotes: 21 | Bounty: $0.00 | Type: 
79. [libcurl stale CURLOPT_AUTOREFERER leaks a previous request URL to a different origin on a reused easy handle](https://hackerone.com/reports/3673277)
   - Program: curl | Upvotes: 22 | Bounty: $0.00 | Type: Information Exposure Through Sent Data
80. [Residual Malicious Payloads on HackerOne after Vulnerability Fixes](https://hackerone.com/reports/3168691)
   - Program: HackerOne | Upvotes: 65 | Bounty: $0.00 | Type: Improper Input Validation
81. [DOS via Mutation Aliasing in GraphQL Account Recovery Phone Number Verification API](https://hackerone.com/reports/3287208)
   - Program: HackerOne | Upvotes: 158 | Bounty: $12500.00 | Type: 
82. [lib/http2.c: SSL connections accept non-HTTP push schemes (incomplete fix for 2e8c922a)](https://hackerone.com/reports/3674275)
   - Program: curl | Upvotes: 30 | Bounty: $0.00 | Type: Authentication Bypass by Primary Weakness
83. [Authorization header leak in ssrf_filter via cross-host redirect leads to credential theft and unauthorized access](https://hackerone.com/reports/3642600)
   - Program: arkadiyt-projects | Upvotes: 40 | Bounty: $0.00 | Type: 
84. [SQL Injection Detection Bypass in AWS WAF Managed Rules (AWSManagedRulesSQLiRuleSet)](https://hackerone.com/reports/3591725)
   - Program: AWS VDP | Upvotes: 36 | Bounty: $0.00 | Type: SQL Injection
85. [DOM XSS in `fizzy.do` import filename preview enables one-click victim account takeover](https://hackerone.com/reports/3608199)
   - Program: Basecamp | Upvotes: 67 | Bounty: $500.00 | Type: Cross-site Scripting (XSS) - DOM
86. [Improper Access Control in `fizzy.do` import flow allows cross-tenant ActionText reference resolution and data disclosure](https://hackerone.com/reports/3543475)
   - Program: Basecamp | Upvotes: 48 | Bounty: $218.00 | Type: Improper Access Control - Generic
87. [BOLA/IDOR in Out-of-Office API allows any authenticated user to read other users' absence data](https://hackerone.com/reports/3382343)
   - Program: Nextcloud | Upvotes: 34 | Bounty: $0.00 | Type: Insecure Direct Object Reference (IDOR)
88. [[Variation of #3321406] YetAnother 1-Click Chaining of Self-XSS, Cookie Tossing and AntiCSRF Token Prediction leads to auto approval in AccessTempAuth](https://hackerone.com/reports/3423950)
   - Program: Cloudflare Public Bug Bounty | Upvotes: 58 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Stored
89. [[Variation of #1554049] 1-Click Chaining of Self-XSS, Cookie Tossing and AntiCSRF Token Prediction leads to auto approval in Access Temp Auth](https://hackerone.com/reports/3321406)
   - Program: Cloudflare Public Bug Bounty | Upvotes: 37 | Bounty: $0.00 | Type: 
90. [Brave Shields Domain Reordering Leads to Origin Confusion](https://hackerone.com/reports/3665151)
   - Program: Brave Software | Upvotes: 50 | Bounty: $0.00 | Type: Violation of Secure Design Principles
91. [Credential Disclosure via Unvalidated directDownloadUrl (Missing DontAddCredentialsAttribute)](https://hackerone.com/reports/3400143)
   - Program: Nextcloud | Upvotes: 37 | Bounty: $250.00 | Type: Insufficiently Protected Credentials
92. [Argument Injection via curl Short-Flag Grouping](https://hackerone.com/reports/3669305)
   - Program: curl | Upvotes: 23 | Bounty: $0.00 | Type: Command Injection - Generic
93. [Integer Overflow/Signedness Mismatch in Printf Precision for HTTP/2 Trailer Headers](https://hackerone.com/reports/3665363)
   - Program: curl | Upvotes: 15 | Bounty: $0.00 | Type: Integer Overflow
94. [Encryption context keys and values logged at INFO level](https://hackerone.com/reports/3620760)
   - Program: AWS VDP | Upvotes: 19 | Bounty: $0.00 | Type: Insertion of Sensitive Information into Log File
95. [Open Redirect in Rocket.Chat](https://hackerone.com/reports/3418031)
   - Program: Rocket.Chat | Upvotes: 32 | Bounty: $0.00 | Type: Open Redirect
96. [[Vertical Privilege Escalation] User can Unapproved any Approved Translation at [/translations/unapprove/]](https://hackerone.com/reports/3020021)
   - Program: Mozilla | Upvotes: 43 | Bounty: $0.00 | Type: Privilege Escalation
97. [User Can Delete Other Users' Personal Access Tokens at /delete-token/{token_id}/ on Mozilla Pontoon](https://hackerone.com/reports/3325582)
   - Program: Mozilla | Upvotes: 38 | Bounty: $0.00 | Type: Improper Access Control - Generic
98. [Memory leak in gem decode logic can allow attacker to take down Rubygems.org application](https://hackerone.com/reports/3079931)
   - Program: RubyGems | Upvotes: 32 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
99. [libcurl: Integer truncation in curl_easy_ssls_import() causes TLS sessions to never expire](https://hackerone.com/reports/3658049)
   - Program: curl | Upvotes: 23 | Bounty: $0.00 | Type: 
100. [Health check errors silently dropped when channel buffer full](https://hackerone.com/reports/3620761)
   - Program: AWS VDP | Upvotes: 22 | Bounty: $0.00 | Type: 
101. [IDOR on ██████ via direct photo URL leads to unauthorized access to deleted and other users' photos](https://hackerone.com/reports/3518758)
   - Program: Nextcloud | Upvotes: 32 | Bounty: $0.00 | Type: Insecure Direct Object Reference (IDOR)
102. [no_proxy IDN mismatch: Unicode hostnames bypass proxy exclusion list](https://hackerone.com/reports/3650443)
   - Program: curl | Upvotes: 15 | Bounty: $0.00 | Type: Improper Access Control - Generic
103. [FTP entrypath accepts 0xFF (Telnet IAC) through incomplete ISCNTRL filter, sent on wire via CWD on connection reuse](https://hackerone.com/reports/3650473)
   - Program: curl | Upvotes: 10 | Bounty: $0.00 | Type: 
104. [Improper enforcement of CURLOPT_SOCKS5_AUTH due to missing reuse key validation in libcurl](https://hackerone.com/reports/3650435)
   - Program: curl | Upvotes: 15 | Bounty: $0.00 | Type: Improper Authorization
105. [Reported Denial of Service](https://hackerone.com/reports/3241102)
   - Program: Monero | Upvotes: 22 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
106. [Reported RPC Overflow](https://hackerone.com/reports/3240792)
   - Program: Monero | Upvotes: 25 | Bounty: $0.00 | Type: Integer Overflow
107. [# SCURLOPT_SSH_KNOWNHOSTS and host fingerprint pins are silently bypassed when an SSH connection is reused from the connection pool](https://hackerone.com/reports/3645415)
   - Program: curl | Upvotes: 9 | Bounty: $0.00 | Type: Exposed Dangerous Method or Function
108. [SMTP Command Injection via CRLF in libcurl MAIL_FROM / MAIL_RCPT (lib/smtp.c)](https://hackerone.com/reports/3651975)
   - Program: curl | Upvotes: 5 | Bounty: $0.00 | Type: CRLF Injection
109. [ignoring 'options' when doing connection reuse](https://hackerone.com/reports/3646914)
   - Program: curl | Upvotes: 9 | Bounty: $0.00 | Type: Incorrect Comparison
110. [Data race in Curl_dnscache_add_negative() corrupts shared DNS cache — heap corruption and double-free when using CURLOPT_SHARE with CURL_LOCK_DATA_DNS](https://hackerone.com/reports/3645361)
   - Program: curl | Upvotes: 23 | Bounty: $0.00 | Type: Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition')
111. [Internal application wrapper or script using curl](https://hackerone.com/reports/3648199)
   - Program: curl | Upvotes: 29 | Bounty: $0.00 | Type: Code Injection
112. [Missing server identity policy enforcement in SSH connection reuse allows host key verification bypass via pool poisoning](https://hackerone.com/reports/3640932)
   - Program: curl | Upvotes: 16 | Bounty: $0.00 | Type: Authentication Bypass by Primary Weakness
113. [Cookie attribute TAB injection regression in Set-Cookie parsing](https://hackerone.com/reports/3641893)
   - Program: curl | Upvotes: 18 | Bounty: $0.00 | Type: Improper Input Validation
114. [Bypassing Strict SSH Server Verification via Connection Pool Reuse in libcurl](https://hackerone.com/reports/3639277)
   - Program: curl | Upvotes: 37 | Bounty: $0.00 | Type: 
115. [Use-After-Free race condition in url_move_hostname() via shared connection pool](https://hackerone.com/reports/3638715)
   - Program: curl | Upvotes: 23 | Bounty: $0.00 | Type: Use After Free
116. [Unauthenticated SSRF via Public Reference API -Sharing Token Bypass](https://hackerone.com/reports/3479692)
   - Program: Nextcloud | Upvotes: 40 | Bounty: $0.00 | Type: 
117. [HackerOne Vulnerability Report: libcurl SSL/TLS Identity Leakage via Insecure Connection Reuse](https://hackerone.com/reports/3636244)
   - Program: curl | Upvotes: 26 | Bounty: $0.00 | Type: Authentication Bypass by Primary Weakness
118. [HTTP/2 PUSH_PROMISE header loss on OOM bypasses scheme validation (regression of 2e8c922a89)](https://hackerone.com/reports/3636044)
   - Program: curl | Upvotes: 15 | Bounty: $0.00 | Type: Improper Handling of Insufficient Permissions or Privileges
119. [Unbounded GZIP Decompression Leading to Event-Loop Starvation](https://hackerone.com/reports/3632427)
   - Program: curl | Upvotes: 17 | Bounty: $0.00 | Type: Improper Handling of Highly Compressed Data (Data Amplification)
120. [SSRF Filter Bypass via Unblocked NAT64 Local-Use IPv6 Prefix (64:ff9b:1::/48)](https://hackerone.com/reports/3634400)
   - Program: arkadiyt-projects | Upvotes: 60 | Bounty: $0.00 | Type: Server-Side Request Forgery (SSRF)
121. [Path Traversal in writeFile via Unsafe Prefix Containment Check Allows Out-of-Directory Writes](https://hackerone.com/reports/3634571)
   - Program: arkadiyt-projects | Upvotes: 21 | Bounty: $0.00 | Type: Path Traversal
122. [HashDoS in V8](https://hackerone.com/reports/3511792)
   - Program: Node.js | Upvotes: 18 | Bounty: $0.00 | Type: Cryptographic Issues - Generic
123. [Permission Model Bypass in realpathSync.native Allows File Existence Disclosure](https://hackerone.com/reports/3480841)
   - Program: Node.js | Upvotes: 14 | Bounty: $0.00 | Type: Information Disclosure
124. [Timing side-channel in HMAC verification via memcmp() in crypto_hmac.cc leads to potential MAC forgery](https://hackerone.com/reports/3533945)
   - Program: Node.js | Upvotes: 15 | Bounty: $0.00 | Type: Cryptographic Issues - Generic
125. [Node.js Permission Model bypass: UDS server bind/listen works without `--allow-net`](https://hackerone.com/reports/3559715)
   - Program: Node.js | Upvotes: 9 | Bounty: $0.00 | Type: Improper Access Control - Generic
126. [Denial of Service via `__proto__` header name in `req.headersDistinct` (Uncaught `TypeError` crashes Node.js process)](https://hackerone.com/reports/3560402)
   - Program: Node.js | Upvotes: 20 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
127. [CVE-2024-36137 Patch Bypass - FileHandle.chmod/chown](https://hackerone.com/reports/3449392)
   - Program: Node.js | Upvotes: 6 | Bounty: $0.00 | Type: Improper Access Control - Generic
128. [Memory leak in Node.js HTTP/2 server via WINDOW_UPDATE on stream 0 leads to resource exhaustion](https://hackerone.com/reports/3531737)
   - Program: Node.js | Upvotes: 6 | Bounty: $0.00 | Type: Missing Release of Memory after Effective Lifetime
129. [CRLF Injection in HAProxy PROXY Protocol via CURLOPT_HAPROXY_CLIENT_IP allows IP spoofing and protocol injection](https://hackerone.com/reports/3633534)
   - Program: curl | Upvotes: 9 | Bounty: $0.00 | Type: CRLF Injection
130. [HTTP/2 server push accepts a non-authoritative :scheme=https over cleartext h2c, enabling HTTPS cache-key poisoning](https://hackerone.com/reports/3630310)
   - Program: curl | Upvotes: 24 | Bounty: $0.00 | Type: Improper Input Validation
131. [Password Strength Policy Bypass via Server-Side Validation Flaw](https://hackerone.com/reports/3523703)
   - Program: Tucows (VDP) | Upvotes: 49 | Bounty: $0.00 | Type: Business Logic Errors
132. [Potential DoS due to PasswordPoliciesNotMet in errors.go](https://hackerone.com/reports/2441029)
   - Program: passhash | Upvotes: 19 | Bounty: $0.00 | Type: 
133. [Missing policies for password in password_policies.go](https://hackerone.com/reports/2439734)
   - Program: passhash | Upvotes: 15 | Bounty: $0.00 | Type: 
134. [Assertion error in node_url.cc via malformed URL format leads to Node.js crash](https://hackerone.com/reports/3546390)
   - Program: Node.js | Upvotes: 39 | Bounty: $0.00 | Type: Reachable Assertion
135. [Server-side ReDoS via user-controlled regex in OIDC Access Policy](https://hackerone.com/reports/3542546)
   - Program: RubyGems | Upvotes: 40 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
136. [Bearer Token Leaked to Attacker via .netrc Despite CVE-2026-3783 Fix](https://hackerone.com/reports/3611825)
   - Program: curl | Upvotes: 23 | Bounty: $0.00 | Type: 
137. [Security Vulnerability Report: Protocol Injection via Programmatic Options](https://hackerone.com/reports/3627638)
   - Program: curl | Upvotes: 13 | Bounty: $0.00 | Type: CRLF Injection
138. [HTTP/1.1 Response Desynchronization via conflicting CL/TE headers in Proxy CONNECT](https://hackerone.com/reports/3623064)
   - Program: curl | Upvotes: 30 | Bounty: $0.00 | Type: HTTP Request Smuggling
139. [Function `do_pubkey()` can have out-of-bound read issue](https://hackerone.com/reports/3617719)
   - Program: curl | Upvotes: 13 | Bounty: $0.00 | Type: Out-of-bounds Read
140. [Potential Subdomain Takeover on IBM.com domain.](https://hackerone.com/reports/3592387)
   - Program: IBM | Upvotes: 77 | Bounty: $0.00 | Type: Improper Access Control - Generic
141. [Access to Deactivated LinkedIn Company Pages via Competitor Analytics API](https://hackerone.com/reports/3604288)
   - Program: LinkedIn | Upvotes: 67 | Bounty: $0.00 | Type: Insecure Direct Object Reference (IDOR)
142. [Fail-Open in set_tlsext_servername_callback on pyopenssl via unhandled exceptions leads to security bypass](https://hackerone.com/reports/3558277)
   - Program: Python Cryptographic Authority | Upvotes: 63 | Bounty: $0.00 | Type: 
143. [[Privilege Escalation] User can Pin|Unpin Any Comment on Any Project or Locale](https://hackerone.com/reports/3025797)
   - Program: Mozilla | Upvotes: 58 | Bounty: $0.00 | Type: Privilege Escalation
144. [Exposed .git/config File Leading to Potential Sensitive Information Disclosure](https://hackerone.com/reports/3612891)
   - Program: curl | Upvotes: 32 | Bounty: $0.00 | Type: 
145. [Add labels to arbitrary issues/prs & compromise github actions label checks](https://hackerone.com/reports/3527771)
   - Program: GitHub | Upvotes: 67 | Bounty: $0.00 | Type: Insecure Direct Object Reference (IDOR)
146. [PATs without the required scope can leak issues](https://hackerone.com/reports/3522254)
   - Program: GitHub | Upvotes: 58 | Bounty: $0.00 | Type: Improper Access Control - Generic
147. [Lack of Validation in Reward Redemption Allows Unlimited Burp Suite License Abuse](https://hackerone.com/reports/3378540)
   - Program: HackerOne | Upvotes: 114 | Bounty: $0.00 | Type: Improper Access Control - Generic
148. [HSTS accepted from HTTP origin behind HTTPS proxy](https://hackerone.com/reports/3609505)
   - Program: curl | Upvotes: 25 | Bounty: $0.00 | Type: Acceptance of Extraneous Untrusted Data With Trusted Data
149. [Unescaped username in SASL DIGEST-MD5 response allows injection](https://hackerone.com/reports/3608522)
   - Program: curl | Upvotes: 26 | Bounty: $0.00 | Type: Improper Neutralization of Escape, Meta, or Control Sequences
150. [Session Cookie Leakage via Static Header Field in WebViewerFragment](https://hackerone.com/reports/3475626)
   - Program: LinkedIn | Upvotes: 120 | Bounty: $0.00 | Type: Misconfiguration
151. [Business Logic Bypass Allows Setting “Read Access” Role Without Pro Plan Subscription](https://hackerone.com/reports/3591764)
   - Program: Lovable VDP | Upvotes: 67 | Bounty: $0.00 | Type: Business Logic Errors
152. [SMB READ_ANDX DataOffset not validated](https://hackerone.com/reports/3603300)
   - Program: curl | Upvotes: 30 | Bounty: $0.00 | Type: 
153. [Unauthenticated access to private files on app.fizzy.do via Active Storage URLs leads to information disclosure](https://hackerone.com/reports/3467641)
   - Program: Basecamp | Upvotes: 63 | Bounty: $100.00 | Type: Insecure Direct Object Reference (IDOR)
154. [Authorization Bypass in Starknet Snap via enableAuthorize parameter leads to unauthorized transaction signing](https://hackerone.com/reports/3507241)
   - Program: MetaMask | Upvotes: 79 | Bounty: $350.00 | Type: Business Logic Errors
155. [SQL Injection vulnerability found on ibm.com endpoint](https://hackerone.com/reports/3578842)
   - Program: IBM | Upvotes: 132 | Bounty: $0.00 | Type: SQL Injection
156. [Curl_compareheader() fails to match multi-value HTTP headers](https://hackerone.com/reports/3598444)
   - Program: curl | Upvotes: 28 | Bounty: $0.00 | Type: Expected Behavior Violation
157. [urlapi: off-by-one in custom scheme validation skips last character](https://hackerone.com/reports/3598358)
   - Program: curl | Upvotes: 38 | Bounty: $0.00 | Type: Off-by-one Error
158. [Bypass of Open Redirect Fix on lovable.dev via /..// Path Traversal in redirect parameter](https://hackerone.com/reports/3599248)
   - Program: Lovable VDP | Upvotes: 68 | Bounty: $0.00 | Type: Open Redirect
159. [NULL Pointer Dereference (DoS) in libcurl SFTP QUOTE command parsing due to missing return statement](https://hackerone.com/reports/3597359)
   - Program: curl | Upvotes: 25 | Bounty: $0.00 | Type: NULL Pointer Dereference
160. [CVE-2026-3805: use after free in SMB connection reuse](https://hackerone.com/reports/3591944)
   - Program: curl | Upvotes: 33 | Bounty: $0.00 | Type: Use After Free
161. [CVE-2026-3784: wrong proxy connection reuse with credentials](https://hackerone.com/reports/3584903)
   - Program: curl | Upvotes: 30 | Bounty: $0.00 | Type: Incorrect Authorization
162. [CVE-2026-3783: token leak with redirect and netrc](https://hackerone.com/reports/3583983)
   - Program: curl | Upvotes: 25 | Bounty: $0.00 | Type: Information Exposure Through Sent Data
163. [Connection Reuse Ignores OAuth Bearer Token Mismatch](https://hackerone.com/reports/3595753)
   - Program: curl | Upvotes: 17 | Bounty: $0.00 | Type: Improper Authentication - Generic
164. [CURLOPT_UNRESTRICTED_AUTH Dangerous Default Documentation Gap](https://hackerone.com/reports/3595764)
   - Program: curl | Upvotes: 18 | Bounty: $0.00 | Type: Information Disclosure
165. [Arbitrary Code Execution via Scanner Bypass in **aws-diagram-mcp-server** `exec()` Namespace](https://hackerone.com/reports/3557138)
   - Program: AWS VDP | Upvotes: 43 | Bounty: $0.00 | Type: 
166. [Users can change project visibility which requires high subscription by just changing request body](https://hackerone.com/reports/3370430)
   - Program: Lovable VDP | Upvotes: 65 | Bounty: $0.00 | Type: Improper Access Control - Generic
167. [LM Challenge-Response Hash Always Sent in SMB Authentication](https://hackerone.com/reports/3584491)
   - Program: curl | Upvotes: 18 | Bounty: $0.00 | Type: Reversible One-Way Hash
168. [In curl's SASL OAUTHBEARER authentication, including the SOH character (0x01) in the username corrupts the message structure.](https://hackerone.com/reports/3584865)
   - Program: curl | Upvotes: 17 | Bounty: $0.00 | Type: Improper Neutralization of Value Delimiters
169. [Injection in path parameter of Ingress-nginx](https://hackerone.com/reports/2701701)
   - Program: Kubernetes | Upvotes: 86 | Bounty: $0.00 | Type: Code Injection
170. [IDOR to make someone attend or leave an event](https://hackerone.com/reports/1734639)
   - Program: LinkedIn | Upvotes: 80 | Bounty: $0.00 | Type: Insecure Direct Object Reference (IDOR)
171. [Blocking a company page admin prevents him from delete paid media admin or edit his roles](https://hackerone.com/reports/2339192)
   - Program: LinkedIn | Upvotes: 54 | Bounty: $0.00 | Type: Improper Access Control - Generic
172. [Open Redirect on lovable.dev via redirect parameter leads to phishing attacks](https://hackerone.com/reports/3581815)
   - Program: Lovable VDP | Upvotes: 43 | Bounty: $0.00 | Type: 
173. [DoS via Unbounded Memory Allocation in sendWebStream on Fastify v5.7.0+ leads to OOM crash when backpressure is ignored](https://hackerone.com/reports/3524779)
   - Program: Fastify | Upvotes: 35 | Bounty: $0.00 | Type: 
174. [Missing Access Control in MigrationFile allows attacker to upload files to any Migration](https://hackerone.com/reports/3506183)
   - Program: GitHub | Upvotes: 85 | Bounty: $0.00 | Type: Insecure Direct Object Reference (IDOR)
175. [SSTI leads to Command injection](https://hackerone.com/reports/3584149)
   - Program: curl | Upvotes: 24 | Bounty: $0.00 | Type: Command Injection - Generic
176. [Use after free in hyperfifo example](https://hackerone.com/reports/3580247)
   - Program: curl | Upvotes: 19 | Bounty: $0.00 | Type: Use After Free
177. [2FA requirement bypass when inviting team members](https://hackerone.com/reports/3356149)
   - Program: Omise | Upvotes: 97 | Bounty: $0.00 | Type: Improper Access Control - Generic
178. [Password Reuse Vulnerability on AWS Sign-in Page via Password Reset Flow leads to Security Policy Violation](https://hackerone.com/reports/3514122)
   - Program: AWS VDP | Upvotes: 54 | Bounty: $0.00 | Type: Weak Password Requirements
179. [Integer Overflow in curl_multi_get_handles() Leading to Heap Buffer Overflow](https://hackerone.com/reports/3575245)
   - Program: curl | Upvotes: 36 | Bounty: $0.00 | Type: Classic Buffer Overflow
180. [RTSP RTP Interleaved Parser Assertion Failure (Zero-Length RTP Payload)](https://hackerone.com/reports/3575250)
   - Program: curl | Upvotes: 28 | Bounty: $0.00 | Type: Improper Check or Handling of Exceptional Conditions
181. [AI Playground XSS to steal user-chat messages and access to connected MCP Server](https://hackerone.com/reports/3424998)
   - Program: Cloudflare Public Bug Bounty | Upvotes: 56 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
182. [Able to bypass HSTS using trailing dot](https://hackerone.com/reports/3574928)
   - Program: curl | Upvotes: 22 | Bounty: $0.00 | Type: Missing Required Cryptographic Step
183. [Curl Telnet Handler Buffer Overflow](https://hackerone.com/reports/3575475)
   - Program: curl | Upvotes: 11 | Bounty: $0.00 | Type: Buffer Underflow
184. [HTML Injection in DAST Trial Request Form Confirmation Email – PortSwigger](https://hackerone.com/reports/3556892)
   - Program: PortSwigger Web Security | Upvotes: 87 | Bounty: $200.00 | Type: 
185. [Publicly accessible `█████████` endpoint exposing internal user identifiers and email addresses](https://hackerone.com/reports/3360293)
   - Program: Mars | Upvotes: 47 | Bounty: $0.00 | Type: Information Disclosure
186. [CVE-█████-35813 in █████](https://hackerone.com/reports/2200329)
   - Program: Mars | Upvotes: 69 | Bounty: $0.00 | Type: Relative Path Traversal
187. [Sensitive information exposed at [███] via /export_panelists_to_xlsx endpoint](https://hackerone.com/reports/3376598)
   - Program: Mars | Upvotes: 33 | Bounty: $0.00 | Type: Cleartext Storage of Sensitive Information
188. [███████ - Publicly Accessible public_html Directory Exposing WordPress Configuration](https://hackerone.com/reports/3066548)
   - Program: Mars | Upvotes: 28 | Bounty: $0.00 | Type: Information Disclosure
189. [SQLi At `███████` via `theme_name`](https://hackerone.com/reports/3293803)
   - Program: Mars | Upvotes: 56 | Bounty: $0.00 | Type: SQL Injection
190. [SQLi at █████ parameter](https://hackerone.com/reports/3277276)
   - Program: Mars | Upvotes: 37 | Bounty: $0.00 | Type: SQL Injection
191. [No Rate Limiting on Password Attempts After Insecure Registration Flow cause ATO](https://hackerone.com/reports/3174778)
   - Program: Mars | Upvotes: 26 | Bounty: $0.00 | Type: Improper Restriction of Authentication Attempts
192. [Unbounded decompression chain in HTTP responses on Node.js Fetch API via Content-Encoding leads to resource exhaustion](https://hackerone.com/reports/3456148)
   - Program: Node.js | Upvotes: 24 | Bounty: $0.00 | Type: 
193. [Splatoon 3 Anticheat Seed Randomization Weakness](https://hackerone.com/reports/3042475)
   - Program: Nintendo | Upvotes: 53 | Bounty: $0.00 | Type: Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG)
194. [ASLR leak in Mario Kart World through LAN mode](https://hackerone.com/reports/3463719)
   - Program: Nintendo | Upvotes: 73 | Bounty: $0.00 | Type: Information Disclosure
195. [XSS Vulnerability on Pressable/Atomic Hosting Platform via unescaped admin notices leads to code execution](https://hackerone.com/reports/3447021)
   - Program: Automattic | Upvotes: 76 | Bounty: $0.00 | Type: 
196. [Improper State Validation on Sony WH-CH520 via BLE Command Service leads to unauthorized Bluetooth pairing and audio hijacking](https://hackerone.com/reports/3514490)
   - Program: Sony | Upvotes: 67 | Bounty: $0.00 | Type: 
197. [TLS PSK/ALPN Callback Exceptions Bypass Error Handlers, Causing DoS and FD Leak](https://hackerone.com/reports/3473882)
   - Program: Node.js | Upvotes: 78 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
198. [Node.js permission model bypass via unchecked Unix Domain Socket connections (UDS)](https://hackerone.com/reports/3465156)
   - Program: Node.js | Upvotes: 49 | Bounty: $0.00 | Type: Server-Side Request Forgery (SSRF)
199. [Uncatchable "Maximum call stack size exceeded" error on Node.js via async_hooks leads to process crashes bypassing error handlers](https://hackerone.com/reports/3456295)
   - Program: Node.js | Upvotes: 34 | Bounty: $0.00 | Type: Improper Handling of Exceptional Conditions
200. [Memory leak that enables remote Denial of Service against applications processing TLS client certificates](https://hackerone.com/reports/3357723)
   - Program: Node.js | Upvotes: 32 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
