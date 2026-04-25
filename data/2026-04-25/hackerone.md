# HackerOne Public Reports Snapshot

Generated: 2026-04-25T14:24:54.012872+00:00

1. [mruby-engine: UAF in MRubyEngine#initialize enables local RCE](https://hackerone.com/reports/3679660)
   - Program: Shopify | Upvotes: 3 | Bounty: $0.00 | Type: 
2. [Incomplete fix for CVE-2026-21637: loadSNI() in _tls_wrap.js lacks try/catch leading to Remote DoS](https://hackerone.com/reports/3556769)
   - Program: Node.js | Upvotes: 18 | Bounty: $0.00 | Type: 
3. [RBAC bypass on App log endpoints via `permissionRequired` typo — any authenticated user reads admin-only Enterprise App logs](https://hackerone.com/reports/3589551)
   - Program: Rocket.Chat | Upvotes: 21 | Bounty: $0.00 | Type: Improper Access Control - Generic
4. [Complete authentication bypass to admin permissions](https://hackerone.com/reports/3564655)
   - Program: Rocket.Chat | Upvotes: 46 | Bounty: $0.00 | Type: SQL Injection
5. [SVG filter primitives bypass remote image blocking, enabling email tracking without consent.](https://hackerone.com/reports/3486747)
   - Program: Nextcloud | Upvotes: 42 | Bounty: $0.00 | Type: Privacy Violation
6. [position: fixed !important bypasses CSS sanitizer's fixed-position mitigation, enabling full-viewport phishing overlays.](https://hackerone.com/reports/3590586)
   - Program: Nextcloud | Upvotes: 37 | Bounty: $0.00 | Type: Resource Injection
7. [Unquoted body background attribute enables CSS injection that bypasses remote image blocking](https://hackerone.com/reports/3590583)
   - Program: Nextcloud | Upvotes: 29 | Bounty: $0.00 | Type: Resource Injection
8. [SMIL values and by attributes bypass remote image blocking via unvalidated resource-loading animations, enabling email tracking without consent](https://hackerone.com/reports/3590576)
   - Program: Nextcloud | Upvotes: 23 | Bounty: $0.00 | Type: Remote File Inclusion
9. [libcurl omits IPv6 zoneid from host identity and leaks credentials/cookies across scoped link-local realms](https://hackerone.com/reports/3680680)
   - Program: curl | Upvotes: 25 | Bounty: $0.00 | Type: Information Disclosure
10. [Digest Auth State Leak on Cross-Origin Redirect via Netrc - Username and Password Hash Sent to Wrong Host](https://hackerone.com/reports/3680038)
   - Program: curl | Upvotes: 12 | Bounty: $0.00 | Type: Insufficiently Protected Credentials
11. [Stored XSS in attachment-display exploitable through SameSite](https://hackerone.com/reports/3594137)
   - Program: Nextcloud | Upvotes: 32 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Stored
12. [libcurl reuses a learned RTSP Session header across different hosts on the same easy handle, enabling cross-host session leak and replay](https://hackerone.com/reports/3680234)
   - Program: curl | Upvotes: 12 | Bounty: $0.00 | Type: Exposure of Data Element to Wrong Session
13. [Rails::HTML::Sanitizer.allowed_uri? returns true for entity-encoded control-character-split javascript: URLs](https://hackerone.com/reports/3601655)
   - Program: Ruby on Rails | Upvotes: 20 | Bounty: $0.00 | Type: 
14. [libcurl stale CURLOPT_AUTOREFERER leaks a previous request URL to a different origin on a reused easy handle](https://hackerone.com/reports/3673277)
   - Program: curl | Upvotes: 21 | Bounty: $0.00 | Type: Information Exposure Through Sent Data
15. [Residual Malicious Payloads on HackerOne after Vulnerability Fixes](https://hackerone.com/reports/3168691)
   - Program: HackerOne | Upvotes: 56 | Bounty: $0.00 | Type: Improper Input Validation
16. [DOS via Mutation Aliasing in GraphQL Account Recovery Phone Number Verification API](https://hackerone.com/reports/3287208)
   - Program: HackerOne | Upvotes: 117 | Bounty: $12500.00 | Type: 
17. [lib/http2.c: SSL connections accept non-HTTP push schemes (incomplete fix for 2e8c922a)](https://hackerone.com/reports/3674275)
   - Program: curl | Upvotes: 25 | Bounty: $0.00 | Type: Authentication Bypass by Primary Weakness
18. [Authorization header leak in ssrf_filter via cross-host redirect leads to credential theft and unauthorized access](https://hackerone.com/reports/3642600)
   - Program: arkadiyt-projects | Upvotes: 38 | Bounty: $0.00 | Type: 
19. [SQL Injection Detection Bypass in AWS WAF Managed Rules (AWSManagedRulesSQLiRuleSet)](https://hackerone.com/reports/3591725)
   - Program: AWS VDP | Upvotes: 31 | Bounty: $0.00 | Type: SQL Injection
20. [DOM XSS in `fizzy.do` import filename preview enables one-click victim account takeover](https://hackerone.com/reports/3608199)
   - Program: Basecamp | Upvotes: 48 | Bounty: $500.00 | Type: Cross-site Scripting (XSS) - DOM
21. [Improper Access Control in `fizzy.do` import flow allows cross-tenant ActionText reference resolution and data disclosure](https://hackerone.com/reports/3543475)
   - Program: Basecamp | Upvotes: 39 | Bounty: $218.00 | Type: Improper Access Control - Generic
22. [BOLA/IDOR in Out-of-Office API allows any authenticated user to read other users' absence data](https://hackerone.com/reports/3382343)
   - Program: Nextcloud | Upvotes: 24 | Bounty: $0.00 | Type: Insecure Direct Object Reference (IDOR)
23. [[Variation of #3321406] YetAnother 1-Click Chaining of Self-XSS, Cookie Tossing and AntiCSRF Token Prediction leads to auto approval in AccessTempAuth](https://hackerone.com/reports/3423950)
   - Program: Cloudflare Public Bug Bounty | Upvotes: 51 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Stored
24. [[Variation of #1554049] 1-Click Chaining of Self-XSS, Cookie Tossing and AntiCSRF Token Prediction leads to auto approval in Access Temp Auth](https://hackerone.com/reports/3321406)
   - Program: Cloudflare Public Bug Bounty | Upvotes: 30 | Bounty: $0.00 | Type: 
25. [Brave Shields Domain Reordering Leads to Origin Confusion](https://hackerone.com/reports/3665151)
   - Program: Brave Software | Upvotes: 44 | Bounty: $100.00 | Type: Violation of Secure Design Principles
26. [Credential Disclosure via Unvalidated directDownloadUrl (Missing DontAddCredentialsAttribute)](https://hackerone.com/reports/3400143)
   - Program: Nextcloud | Upvotes: 34 | Bounty: $250.00 | Type: Insufficiently Protected Credentials
27. [Argument Injection via curl Short-Flag Grouping](https://hackerone.com/reports/3669305)
   - Program: curl | Upvotes: 21 | Bounty: $0.00 | Type: Command Injection - Generic
28. [Integer Overflow/Signedness Mismatch in Printf Precision for HTTP/2 Trailer Headers](https://hackerone.com/reports/3665363)
   - Program: curl | Upvotes: 15 | Bounty: $0.00 | Type: Integer Overflow
29. [Encryption context keys and values logged at INFO level](https://hackerone.com/reports/3620760)
   - Program: AWS VDP | Upvotes: 18 | Bounty: $0.00 | Type: Insertion of Sensitive Information into Log File
30. [Open Redirect in Rocket.Chat](https://hackerone.com/reports/3418031)
   - Program: Rocket.Chat | Upvotes: 30 | Bounty: $0.00 | Type: Open Redirect
31. [[Vertical Privilege Escalation] User can Unapproved any Approved Translation at [/translations/unapprove/]](https://hackerone.com/reports/3020021)
   - Program: Mozilla | Upvotes: 40 | Bounty: $0.00 | Type: Privilege Escalation
32. [User Can Delete Other Users' Personal Access Tokens at /delete-token/{token_id}/ on Mozilla Pontoon](https://hackerone.com/reports/3325582)
   - Program: Mozilla | Upvotes: 34 | Bounty: $0.00 | Type: Improper Access Control - Generic
33. [Memory leak in gem decode logic can allow attacker to take down Rubygems.org application](https://hackerone.com/reports/3079931)
   - Program: RubyGems | Upvotes: 31 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
34. [libcurl: Integer truncation in curl_easy_ssls_import() causes TLS sessions to never expire](https://hackerone.com/reports/3658049)
   - Program: curl | Upvotes: 23 | Bounty: $0.00 | Type: 
35. [Health check errors silently dropped when channel buffer full](https://hackerone.com/reports/3620761)
   - Program: AWS VDP | Upvotes: 21 | Bounty: $0.00 | Type: 
36. [IDOR on ██████ via direct photo URL leads to unauthorized access to deleted and other users' photos](https://hackerone.com/reports/3518758)
   - Program: Nextcloud | Upvotes: 30 | Bounty: $0.00 | Type: Insecure Direct Object Reference (IDOR)
37. [no_proxy IDN mismatch: Unicode hostnames bypass proxy exclusion list](https://hackerone.com/reports/3650443)
   - Program: curl | Upvotes: 15 | Bounty: $0.00 | Type: Improper Access Control - Generic
38. [FTP entrypath accepts 0xFF (Telnet IAC) through incomplete ISCNTRL filter, sent on wire via CWD on connection reuse](https://hackerone.com/reports/3650473)
   - Program: curl | Upvotes: 9 | Bounty: $0.00 | Type: 
39. [Improper enforcement of CURLOPT_SOCKS5_AUTH due to missing reuse key validation in libcurl](https://hackerone.com/reports/3650435)
   - Program: curl | Upvotes: 14 | Bounty: $0.00 | Type: Improper Authorization
40. [Reported Denial of Service](https://hackerone.com/reports/3241102)
   - Program: Monero | Upvotes: 21 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
41. [Reported RPC Overflow](https://hackerone.com/reports/3240792)
   - Program: Monero | Upvotes: 25 | Bounty: $0.00 | Type: Integer Overflow
42. [# SCURLOPT_SSH_KNOWNHOSTS and host fingerprint pins are silently bypassed when an SSH connection is reused from the connection pool](https://hackerone.com/reports/3645415)
   - Program: curl | Upvotes: 8 | Bounty: $0.00 | Type: Exposed Dangerous Method or Function
43. [SMTP Command Injection via CRLF in libcurl MAIL_FROM / MAIL_RCPT (lib/smtp.c)](https://hackerone.com/reports/3651975)
   - Program: curl | Upvotes: 4 | Bounty: $0.00 | Type: CRLF Injection
44. [ignoring 'options' when doing connection reuse](https://hackerone.com/reports/3646914)
   - Program: curl | Upvotes: 8 | Bounty: $0.00 | Type: Incorrect Comparison
45. [Data race in Curl_dnscache_add_negative() corrupts shared DNS cache — heap corruption and double-free when using CURLOPT_SHARE with CURL_LOCK_DATA_DNS](https://hackerone.com/reports/3645361)
   - Program: curl | Upvotes: 22 | Bounty: $0.00 | Type: Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition')
46. [Internal application wrapper or script using curl](https://hackerone.com/reports/3648199)
   - Program: curl | Upvotes: 27 | Bounty: $0.00 | Type: Code Injection
47. [Missing server identity policy enforcement in SSH connection reuse allows host key verification bypass via pool poisoning](https://hackerone.com/reports/3640932)
   - Program: curl | Upvotes: 16 | Bounty: $0.00 | Type: Authentication Bypass by Primary Weakness
48. [Cookie attribute TAB injection regression in Set-Cookie parsing](https://hackerone.com/reports/3641893)
   - Program: curl | Upvotes: 18 | Bounty: $0.00 | Type: Improper Input Validation
49. [Bypassing Strict SSH Server Verification via Connection Pool Reuse in libcurl](https://hackerone.com/reports/3639277)
   - Program: curl | Upvotes: 34 | Bounty: $0.00 | Type: 
50. [Use-After-Free race condition in url_move_hostname() via shared connection pool](https://hackerone.com/reports/3638715)
   - Program: curl | Upvotes: 23 | Bounty: $0.00 | Type: Use After Free
51. [Unauthenticated SSRF via Public Reference API -Sharing Token Bypass](https://hackerone.com/reports/3479692)
   - Program: Nextcloud | Upvotes: 39 | Bounty: $0.00 | Type: 
52. [HackerOne Vulnerability Report: libcurl SSL/TLS Identity Leakage via Insecure Connection Reuse](https://hackerone.com/reports/3636244)
   - Program: curl | Upvotes: 25 | Bounty: $0.00 | Type: Authentication Bypass by Primary Weakness
53. [HTTP/2 PUSH_PROMISE header loss on OOM bypasses scheme validation (regression of 2e8c922a89)](https://hackerone.com/reports/3636044)
   - Program: curl | Upvotes: 14 | Bounty: $0.00 | Type: Improper Handling of Insufficient Permissions or Privileges
54. [Unbounded GZIP Decompression Leading to Event-Loop Starvation](https://hackerone.com/reports/3632427)
   - Program: curl | Upvotes: 15 | Bounty: $0.00 | Type: Improper Handling of Highly Compressed Data (Data Amplification)
55. [SSRF Filter Bypass via Unblocked NAT64 Local-Use IPv6 Prefix (64:ff9b:1::/48)](https://hackerone.com/reports/3634400)
   - Program: arkadiyt-projects | Upvotes: 54 | Bounty: $0.00 | Type: Server-Side Request Forgery (SSRF)
56. [Path Traversal in writeFile via Unsafe Prefix Containment Check Allows Out-of-Directory Writes](https://hackerone.com/reports/3634571)
   - Program: arkadiyt-projects | Upvotes: 20 | Bounty: $0.00 | Type: Path Traversal
57. [HashDoS in V8](https://hackerone.com/reports/3511792)
   - Program: Node.js | Upvotes: 17 | Bounty: $0.00 | Type: Cryptographic Issues - Generic
58. [Permission Model Bypass in realpathSync.native Allows File Existence Disclosure](https://hackerone.com/reports/3480841)
   - Program: Node.js | Upvotes: 14 | Bounty: $0.00 | Type: Information Disclosure
59. [Timing side-channel in HMAC verification via memcmp() in crypto_hmac.cc leads to potential MAC forgery](https://hackerone.com/reports/3533945)
   - Program: Node.js | Upvotes: 15 | Bounty: $0.00 | Type: Cryptographic Issues - Generic
60. [Node.js Permission Model bypass: UDS server bind/listen works without `--allow-net`](https://hackerone.com/reports/3559715)
   - Program: Node.js | Upvotes: 9 | Bounty: $0.00 | Type: Improper Access Control - Generic
61. [Denial of Service via `__proto__` header name in `req.headersDistinct` (Uncaught `TypeError` crashes Node.js process)](https://hackerone.com/reports/3560402)
   - Program: Node.js | Upvotes: 19 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
62. [CVE-2024-36137 Patch Bypass - FileHandle.chmod/chown](https://hackerone.com/reports/3449392)
   - Program: Node.js | Upvotes: 6 | Bounty: $0.00 | Type: Improper Access Control - Generic
63. [Memory leak in Node.js HTTP/2 server via WINDOW_UPDATE on stream 0 leads to resource exhaustion](https://hackerone.com/reports/3531737)
   - Program: Node.js | Upvotes: 6 | Bounty: $0.00 | Type: Missing Release of Memory after Effective Lifetime
64. [CRLF Injection in HAProxy PROXY Protocol via CURLOPT_HAPROXY_CLIENT_IP allows IP spoofing and protocol injection](https://hackerone.com/reports/3633534)
   - Program: curl | Upvotes: 9 | Bounty: $0.00 | Type: CRLF Injection
65. [HTTP/2 server push accepts a non-authoritative :scheme=https over cleartext h2c, enabling HTTPS cache-key poisoning](https://hackerone.com/reports/3630310)
   - Program: curl | Upvotes: 24 | Bounty: $0.00 | Type: Improper Input Validation
66. [Password Strength Policy Bypass via Server-Side Validation Flaw](https://hackerone.com/reports/3523703)
   - Program: Tucows (VDP) | Upvotes: 46 | Bounty: $0.00 | Type: Business Logic Errors
67. [Potential DoS due to PasswordPoliciesNotMet in errors.go](https://hackerone.com/reports/2441029)
   - Program: passhash | Upvotes: 19 | Bounty: $0.00 | Type: 
68. [Missing policies for password in password_policies.go](https://hackerone.com/reports/2439734)
   - Program: passhash | Upvotes: 15 | Bounty: $0.00 | Type: 
69. [Assertion error in node_url.cc via malformed URL format leads to Node.js crash](https://hackerone.com/reports/3546390)
   - Program: Node.js | Upvotes: 39 | Bounty: $0.00 | Type: Reachable Assertion
70. [Server-side ReDoS via user-controlled regex in OIDC Access Policy](https://hackerone.com/reports/3542546)
   - Program: RubyGems | Upvotes: 40 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
71. [Bearer Token Leaked to Attacker via .netrc Despite CVE-2026-3783 Fix](https://hackerone.com/reports/3611825)
   - Program: curl | Upvotes: 23 | Bounty: $0.00 | Type: 
72. [Security Vulnerability Report: Protocol Injection via Programmatic Options](https://hackerone.com/reports/3627638)
   - Program: curl | Upvotes: 13 | Bounty: $0.00 | Type: CRLF Injection
73. [HTTP/1.1 Response Desynchronization via conflicting CL/TE headers in Proxy CONNECT](https://hackerone.com/reports/3623064)
   - Program: curl | Upvotes: 30 | Bounty: $0.00 | Type: HTTP Request Smuggling
74. [Function `do_pubkey()` can have out-of-bound read issue](https://hackerone.com/reports/3617719)
   - Program: curl | Upvotes: 13 | Bounty: $0.00 | Type: Out-of-bounds Read
75. [Potential Subdomain Takeover on IBM.com domain.](https://hackerone.com/reports/3592387)
   - Program: IBM | Upvotes: 72 | Bounty: $0.00 | Type: Improper Access Control - Generic
76. [Access to Deactivated LinkedIn Company Pages via Competitor Analytics API](https://hackerone.com/reports/3604288)
   - Program: LinkedIn | Upvotes: 64 | Bounty: $0.00 | Type: Insecure Direct Object Reference (IDOR)
77. [Fail-Open in set_tlsext_servername_callback on pyopenssl via unhandled exceptions leads to security bypass](https://hackerone.com/reports/3558277)
   - Program: Python Cryptographic Authority | Upvotes: 63 | Bounty: $0.00 | Type: 
78. [[Privilege Escalation] User can Pin|Unpin Any Comment on Any Project or Locale](https://hackerone.com/reports/3025797)
   - Program: Mozilla | Upvotes: 56 | Bounty: $0.00 | Type: Privilege Escalation
79. [Exposed .git/config File Leading to Potential Sensitive Information Disclosure](https://hackerone.com/reports/3612891)
   - Program: curl | Upvotes: 33 | Bounty: $0.00 | Type: 
80. [Add labels to arbitrary issues/prs & compromise github actions label checks](https://hackerone.com/reports/3527771)
   - Program: GitHub | Upvotes: 65 | Bounty: $0.00 | Type: Insecure Direct Object Reference (IDOR)
81. [PATs without the required scope can leak issues](https://hackerone.com/reports/3522254)
   - Program: GitHub | Upvotes: 57 | Bounty: $0.00 | Type: Improper Access Control - Generic
82. [Lack of Validation in Reward Redemption Allows Unlimited Burp Suite License Abuse](https://hackerone.com/reports/3378540)
   - Program: HackerOne | Upvotes: 111 | Bounty: $0.00 | Type: Improper Access Control - Generic
83. [HSTS accepted from HTTP origin behind HTTPS proxy](https://hackerone.com/reports/3609505)
   - Program: curl | Upvotes: 25 | Bounty: $0.00 | Type: Acceptance of Extraneous Untrusted Data With Trusted Data
84. [Unescaped username in SASL DIGEST-MD5 response allows injection](https://hackerone.com/reports/3608522)
   - Program: curl | Upvotes: 26 | Bounty: $0.00 | Type: Improper Neutralization of Escape, Meta, or Control Sequences
85. [Session Cookie Leakage via Static Header Field in WebViewerFragment](https://hackerone.com/reports/3475626)
   - Program: LinkedIn | Upvotes: 114 | Bounty: $0.00 | Type: Misconfiguration
86. [Business Logic Bypass Allows Setting “Read Access” Role Without Pro Plan Subscription](https://hackerone.com/reports/3591764)
   - Program: Lovable VDP | Upvotes: 64 | Bounty: $0.00 | Type: Business Logic Errors
87. [SMB READ_ANDX DataOffset not validated](https://hackerone.com/reports/3603300)
   - Program: curl | Upvotes: 30 | Bounty: $0.00 | Type: 
88. [Unauthenticated access to private files on app.fizzy.do via Active Storage URLs leads to information disclosure](https://hackerone.com/reports/3467641)
   - Program: Basecamp | Upvotes: 61 | Bounty: $100.00 | Type: Insecure Direct Object Reference (IDOR)
89. [Authorization Bypass in Starknet Snap via enableAuthorize parameter leads to unauthorized transaction signing](https://hackerone.com/reports/3507241)
   - Program: Consensys | Upvotes: 79 | Bounty: $0.00 | Type: Business Logic Errors
90. [SQL Injection vulnerability found on ibm.com endpoint](https://hackerone.com/reports/3578842)
   - Program: IBM | Upvotes: 125 | Bounty: $0.00 | Type: SQL Injection
91. [Curl_compareheader() fails to match multi-value HTTP headers](https://hackerone.com/reports/3598444)
   - Program: curl | Upvotes: 28 | Bounty: $0.00 | Type: Expected Behavior Violation
92. [urlapi: off-by-one in custom scheme validation skips last character](https://hackerone.com/reports/3598358)
   - Program: curl | Upvotes: 38 | Bounty: $0.00 | Type: Off-by-one Error
93. [Bypass of Open Redirect Fix on lovable.dev via /..// Path Traversal in redirect parameter](https://hackerone.com/reports/3599248)
   - Program: Lovable VDP | Upvotes: 66 | Bounty: $0.00 | Type: Open Redirect
94. [NULL Pointer Dereference (DoS) in libcurl SFTP QUOTE command parsing due to missing return statement](https://hackerone.com/reports/3597359)
   - Program: curl | Upvotes: 25 | Bounty: $0.00 | Type: NULL Pointer Dereference
95. [CVE-2026-3805: use after free in SMB connection reuse](https://hackerone.com/reports/3591944)
   - Program: curl | Upvotes: 33 | Bounty: $0.00 | Type: Use After Free
96. [CVE-2026-3784: wrong proxy connection reuse with credentials](https://hackerone.com/reports/3584903)
   - Program: curl | Upvotes: 30 | Bounty: $0.00 | Type: Incorrect Authorization
97. [CVE-2026-3783: token leak with redirect and netrc](https://hackerone.com/reports/3583983)
   - Program: curl | Upvotes: 25 | Bounty: $0.00 | Type: Information Exposure Through Sent Data
98. [Connection Reuse Ignores OAuth Bearer Token Mismatch](https://hackerone.com/reports/3595753)
   - Program: curl | Upvotes: 17 | Bounty: $0.00 | Type: Improper Authentication - Generic
99. [CURLOPT_UNRESTRICTED_AUTH Dangerous Default Documentation Gap](https://hackerone.com/reports/3595764)
   - Program: curl | Upvotes: 18 | Bounty: $0.00 | Type: Information Disclosure
100. [Arbitrary Code Execution via Scanner Bypass in **aws-diagram-mcp-server** `exec()` Namespace](https://hackerone.com/reports/3557138)
   - Program: AWS VDP | Upvotes: 42 | Bounty: $0.00 | Type: 
101. [Users can change project visibility which requires high subscription by just changing request body](https://hackerone.com/reports/3370430)
   - Program: Lovable VDP | Upvotes: 62 | Bounty: $0.00 | Type: Improper Access Control - Generic
102. [LM Challenge-Response Hash Always Sent in SMB Authentication](https://hackerone.com/reports/3584491)
   - Program: curl | Upvotes: 18 | Bounty: $0.00 | Type: Reversible One-Way Hash
103. [In curl's SASL OAUTHBEARER authentication, including the SOH character (0x01) in the username corrupts the message structure.](https://hackerone.com/reports/3584865)
   - Program: curl | Upvotes: 17 | Bounty: $0.00 | Type: Improper Neutralization of Value Delimiters
104. [Injection in path parameter of Ingress-nginx](https://hackerone.com/reports/2701701)
   - Program: Kubernetes | Upvotes: 82 | Bounty: $0.00 | Type: Code Injection
105. [IDOR to make someone attend or leave an event](https://hackerone.com/reports/1734639)
   - Program: LinkedIn | Upvotes: 78 | Bounty: $0.00 | Type: Insecure Direct Object Reference (IDOR)
106. [Blocking a company page admin prevents him from delete paid media admin or edit his roles](https://hackerone.com/reports/2339192)
   - Program: LinkedIn | Upvotes: 51 | Bounty: $0.00 | Type: Improper Access Control - Generic
107. [Open Redirect on lovable.dev via redirect parameter leads to phishing attacks](https://hackerone.com/reports/3581815)
   - Program: Lovable VDP | Upvotes: 41 | Bounty: $0.00 | Type: 
108. [DoS via Unbounded Memory Allocation in sendWebStream on Fastify v5.7.0+ leads to OOM crash when backpressure is ignored](https://hackerone.com/reports/3524779)
   - Program: Fastify | Upvotes: 35 | Bounty: $0.00 | Type: 
109. [Missing Access Control in MigrationFile allows attacker to upload files to any Migration](https://hackerone.com/reports/3506183)
   - Program: GitHub | Upvotes: 82 | Bounty: $0.00 | Type: Insecure Direct Object Reference (IDOR)
110. [SSTI leads to Command injection](https://hackerone.com/reports/3584149)
   - Program: curl | Upvotes: 24 | Bounty: $0.00 | Type: Command Injection - Generic
111. [Use after free in hyperfifo example](https://hackerone.com/reports/3580247)
   - Program: curl | Upvotes: 19 | Bounty: $0.00 | Type: Use After Free
112. [2FA requirement bypass when inviting team members](https://hackerone.com/reports/3356149)
   - Program: Omise | Upvotes: 92 | Bounty: $0.00 | Type: Improper Access Control - Generic
113. [Password Reuse Vulnerability on AWS Sign-in Page via Password Reset Flow leads to Security Policy Violation](https://hackerone.com/reports/3514122)
   - Program: AWS VDP | Upvotes: 54 | Bounty: $0.00 | Type: Weak Password Requirements
114. [Integer Overflow in curl_multi_get_handles() Leading to Heap Buffer Overflow](https://hackerone.com/reports/3575245)
   - Program: curl | Upvotes: 36 | Bounty: $0.00 | Type: Classic Buffer Overflow
115. [RTSP RTP Interleaved Parser Assertion Failure (Zero-Length RTP Payload)](https://hackerone.com/reports/3575250)
   - Program: curl | Upvotes: 28 | Bounty: $0.00 | Type: Improper Check or Handling of Exceptional Conditions
116. [AI Playground XSS to steal user-chat messages and access to connected MCP Server](https://hackerone.com/reports/3424998)
   - Program: Cloudflare Public Bug Bounty | Upvotes: 52 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
117. [Able to bypass HSTS using trailing dot](https://hackerone.com/reports/3574928)
   - Program: curl | Upvotes: 22 | Bounty: $0.00 | Type: Missing Required Cryptographic Step
118. [Curl Telnet Handler Buffer Overflow](https://hackerone.com/reports/3575475)
   - Program: curl | Upvotes: 11 | Bounty: $0.00 | Type: Buffer Underflow
119. [HTML Injection in DAST Trial Request Form Confirmation Email – PortSwigger](https://hackerone.com/reports/3556892)
   - Program: PortSwigger Web Security | Upvotes: 86 | Bounty: $200.00 | Type: 
120. [Publicly accessible `█████████` endpoint exposing internal user identifiers and email addresses](https://hackerone.com/reports/3360293)
   - Program: Mars | Upvotes: 46 | Bounty: $0.00 | Type: Information Disclosure
121. [CVE-█████-35813 in █████](https://hackerone.com/reports/2200329)
   - Program: Mars | Upvotes: 67 | Bounty: $0.00 | Type: Relative Path Traversal
122. [Sensitive information exposed at [███] via /export_panelists_to_xlsx endpoint](https://hackerone.com/reports/3376598)
   - Program: Mars | Upvotes: 33 | Bounty: $0.00 | Type: Cleartext Storage of Sensitive Information
123. [███████ - Publicly Accessible public_html Directory Exposing WordPress Configuration](https://hackerone.com/reports/3066548)
   - Program: Mars | Upvotes: 28 | Bounty: $0.00 | Type: Information Disclosure
124. [SQLi At `███████` via `theme_name`](https://hackerone.com/reports/3293803)
   - Program: Mars | Upvotes: 50 | Bounty: $0.00 | Type: SQL Injection
125. [SQLi at █████ parameter](https://hackerone.com/reports/3277276)
   - Program: Mars | Upvotes: 34 | Bounty: $0.00 | Type: SQL Injection
126. [No Rate Limiting on Password Attempts After Insecure Registration Flow cause ATO](https://hackerone.com/reports/3174778)
   - Program: Mars | Upvotes: 26 | Bounty: $0.00 | Type: Improper Restriction of Authentication Attempts
127. [Unbounded decompression chain in HTTP responses on Node.js Fetch API via Content-Encoding leads to resource exhaustion](https://hackerone.com/reports/3456148)
   - Program: Node.js | Upvotes: 24 | Bounty: $0.00 | Type: 
128. [Splatoon 3 Anticheat Seed Randomization Weakness](https://hackerone.com/reports/3042475)
   - Program: Nintendo | Upvotes: 53 | Bounty: $0.00 | Type: Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG)
129. [ASLR leak in Mario Kart World through LAN mode](https://hackerone.com/reports/3463719)
   - Program: Nintendo | Upvotes: 73 | Bounty: $0.00 | Type: Information Disclosure
130. [XSS Vulnerability on Pressable/Atomic Hosting Platform via unescaped admin notices leads to code execution](https://hackerone.com/reports/3447021)
   - Program: Automattic | Upvotes: 76 | Bounty: $0.00 | Type: 
131. [Improper State Validation on Sony WH-CH520 via BLE Command Service leads to unauthorized Bluetooth pairing and audio hijacking](https://hackerone.com/reports/3514490)
   - Program: Sony | Upvotes: 67 | Bounty: $0.00 | Type: 
132. [TLS PSK/ALPN Callback Exceptions Bypass Error Handlers, Causing DoS and FD Leak](https://hackerone.com/reports/3473882)
   - Program: Node.js | Upvotes: 78 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
133. [Node.js permission model bypass via unchecked Unix Domain Socket connections (UDS)](https://hackerone.com/reports/3465156)
   - Program: Node.js | Upvotes: 48 | Bounty: $0.00 | Type: Server-Side Request Forgery (SSRF)
134. [Uncatchable "Maximum call stack size exceeded" error on Node.js via async_hooks leads to process crashes bypassing error handlers](https://hackerone.com/reports/3456295)
   - Program: Node.js | Upvotes: 34 | Bounty: $0.00 | Type: Improper Handling of Exceptional Conditions
135. [Memory leak that enables remote Denial of Service against applications processing TLS client certificates](https://hackerone.com/reports/3357723)
   - Program: Node.js | Upvotes: 32 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
136. [Timeout-based race conditions make Uint8Array/Buffer.alloc non-zerofilled](https://hackerone.com/reports/3405778)
   - Program: Node.js | Upvotes: 42 | Bounty: $0.00 | Type: Improper Initialization
137. [FS Permissions Bypass](https://hackerone.com/reports/3417819)
   - Program: Node.js | Upvotes: 33 | Bounty: $0.00 | Type: Violation of Secure Design Principles
138. [Mail stored HTML injection in subject text](https://hackerone.com/reports/3357036)
   - Program: Nextcloud | Upvotes: 46 | Bounty: $350.00 | Type: 
139. [Cache Pollution via Unkeyed GET Parameters on www.omise.co](https://hackerone.com/reports/3183046)
   - Program: Omise | Upvotes: 43 | Bounty: $0.00 | Type: 
140. [Unlimited Reuse of Coupon Code Allows Free Shipping on All Orders on ██████████](https://hackerone.com/reports/3426839)
   - Program: AWS VDP | Upvotes: 66 | Bounty: $0.00 | Type: Business Logic Errors
141. [ASGIRequest header concatenation quadratic CPU DoS on Django via repeated headers leads to worker exhaustion](https://hackerone.com/reports/3426417)
   - Program: Django | Upvotes: 24 | Bounty: $0.00 | Type: 
142. [WebAuthn app was updated based on public key](https://hackerone.com/reports/3360354)
   - Program: Nextcloud | Upvotes: 81 | Bounty: $750.00 | Type: Insecure Direct Object Reference (IDOR)
143. [MQTT Protocol Packet Injection via Unchecked CONNACK Remaining Length](https://hackerone.com/reports/3531216)
   - Program: curl | Upvotes: 45 | Bounty: $0.00 | Type: 
144. [User enumeration via timing attack in Django mod_wsgi authentication backend leads to account discovery](https://hackerone.com/reports/3424977)
   - Program: Django | Upvotes: 61 | Bounty: $0.00 | Type: 
145. [Information Disclosure via Logback Configuration Injection in GoCD Agent](https://hackerone.com/reports/3509632)
   - Program: GoCD | Upvotes: 36 | Bounty: $0.00 | Type: Information Disclosure
146. [Previous commentor on post can still comment even after comment permission is changed to disabled](https://hackerone.com/reports/3151001)
   - Program: LinkedIn | Upvotes: 108 | Bounty: $0.00 | Type: Improper Access Control - Generic
147. [Improper Access Control - Access to "Active Hiring" (Premium  feature) filter results](https://hackerone.com/reports/3235855)
   - Program: LinkedIn | Upvotes: 94 | Bounty: $0.00 | Type: Improper Access Control - Generic
148. [SQL injection in structure plugin](https://hackerone.com/reports/3249794)
   - Program: ExpressionEngine | Upvotes: 122 | Bounty: $0.00 | Type: SQL Injection
149. [wcurl Argument Injection via Unquoted Variable](https://hackerone.com/reports/3523953)
   - Program: curl | Upvotes: 43 | Bounty: $0.00 | Type: Command Injection - Generic
150. [Integer Underflow in src/var.c](https://hackerone.com/reports/3523349)
   - Program: curl | Upvotes: 46 | Bounty: $0.00 | Type: Integer Underflow
151. [Spam & Clearance checks disabled with existing referenced Message-ID](https://hackerone.com/reports/2012659)
   - Program: Basecamp | Upvotes: 117 | Bounty: $250.00 | Type: Improper Access Control - Generic
152. [[Critical] Unauthorized Cross-Tenant Data Access in Stripo AI Hub Campaign via Deleted Project.](https://hackerone.com/reports/3459285)
   - Program: Stripo Inc | Upvotes: 135 | Bounty: $0.00 | Type: Improper Access Control - Generic
153. [Memory Exhaustion in CometBFT v1.0.1 via malicious ProposalMessage leads to network-wide denial of service](https://hackerone.com/reports/3510161)
   - Program: Cosmos | Upvotes: 46 | Bounty: $0.00 | Type: 
154. [Cross‑origin cookies leak and injection risk when using a custom Host header](https://hackerone.com/reports/3516878)
   - Program: curl | Upvotes: 30 | Bounty: $0.00 | Type: Insufficiently Protected Credentials
155. [SSL options ISSUERCERT, EC_CURVES and CRLFILE silently ignored by non-OpenSSL backends](https://hackerone.com/reports/3516974)
   - Program: curl | Upvotes: 31 | Bounty: $0.00 | Type: Missing Required Cryptographic Step
156. [Internal logs/info leaked via endpoint {https://203.137.128.240/server-status}](https://hackerone.com/reports/2473173)
   - Program: pixiv | Upvotes: 140 | Bounty: $0.00 | Type: Information Disclosure
157. [Cookie Replacement Use-After-Free Vulnerability](https://hackerone.com/reports/3516202)
   - Program: curl | Upvotes: 21 | Bounty: $0.00 | Type: Use After Free
158. [Cookie Max-Age Integer Overflow Vulnerability](https://hackerone.com/reports/3516186)
   - Program: curl | Upvotes: 28 | Bounty: $0.00 | Type: Integer Overflow
159. [Disclose Hidden Comments on Media Section of hub.vroid.com](https://hackerone.com/reports/2541962)
   - Program: pixiv | Upvotes: 127 | Bounty: $500.00 | Type: Insecure Direct Object Reference (IDOR)
160. [clickjacing can lead to account takeover](https://hackerone.com/reports/2119892)
   - Program: pixiv | Upvotes: 65 | Bounty: $200.00 | Type: UI Redressing (Clickjacking)
161. [libcurl: Improper Authentication State Management on Cross-Protocol Redirects](https://hackerone.com/reports/3514263)
   - Program: curl | Upvotes: 17 | Bounty: $0.00 | Type: Insufficiently Protected Credentials
162. [Easy way to create a new Deck board without permission](https://hackerone.com/reports/2388183)
   - Program: Nextcloud | Upvotes: 56 | Bounty: $100.00 | Type: Improper Access Control - Generic
163. [Can download files on Android app without permission](https://hackerone.com/reports/2380133)
   - Program: Nextcloud | Upvotes: 46 | Bounty: $250.00 | Type: Improper Access Control - Generic
164. [Command Injection on Amazon Q Developer CLI via malicious .amazonq/mcp.json leads to arbitrary code execution](https://hackerone.com/reports/3427370)
   - Program: AWS VDP | Upvotes: 19 | Bounty: $0.00 | Type: Command Injection - Generic
165. [fs.futimes() Bypasses Read-Only Permission Model](https://hackerone.com/reports/3390084)
   - Program: Node.js | Upvotes: 33 | Bounty: $0.00 | Type: Improper Access Control - Generic
166. [IMAP Protocol Desynchronization and Response Smuggling via Naive Literal Parsing](https://hackerone.com/reports/3509396)
   - Program: curl | Upvotes: 14 | Bounty: $0.00 | Type: Improper Input Validation
167. [Roundcube Webmail Style Sanitizer can be bypassed using CSS Character Escapes](https://hackerone.com/reports/3443563)
   - Program: Nextcloud | Upvotes: 46 | Bounty: $0.00 | Type: Information Disclosure
168. [[revive-adserver] Reflected XSS in Banner Delivery Options via cap parameter](https://hackerone.com/reports/3473696)
   - Program: Revive Adserver | Upvotes: 35 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
169. [Reflected XSS in banner-acl.php and channel-acl.php via executionorder](https://hackerone.com/reports/3470970)
   - Program: Revive Adserver | Upvotes: 37 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
170. [Reflected XSS in afr.php](https://hackerone.com/reports/3468169)
   - Program: Revive Adserver | Upvotes: 34 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
171. [Broken Access Control allows advertiser accounts to delete trackers they do not own](https://hackerone.com/reports/3445710)
   - Program: Revive Adserver | Upvotes: 45 | Bounty: $0.00 | Type: Improper Access Control - Generic
172. [INI Format string injection in Revive Adserver 6.0.4 settings](https://hackerone.com/reports/3445332)
   - Program: Revive Adserver | Upvotes: 19 | Bounty: $0.00 | Type: Use of Externally-Controlled Format String
173. [Integer-underflow leads to heap over-read in TFTP implementation](https://hackerone.com/reports/3508321)
   - Program: curl | Upvotes: 7 | Bounty: $0.00 | Type: Buffer Over-read
174. [Digest Authentication Header Injection](https://hackerone.com/reports/3508799)
   - Program: curl | Upvotes: 8 | Bounty: $0.00 | Type: HTTP Response Splitting
175. [Directory listing vulnerability is disclosing names and emails, widespread (thousands of records, publicly accessible without auth)](https://hackerone.com/reports/3509437)
   - Program: curl | Upvotes: 10 | Bounty: $0.00 | Type: Information Exposure Through Directory Listing
176. [Gopher Protocol Command Injection (SSRF Smuggling)](https://hackerone.com/reports/3508785)
   - Program: curl | Upvotes: 6 | Bounty: $0.00 | Type: Server-Side Request Forgery (SSRF)
177. [Use-After-Free in curl_easy_nextheader when reusing header handle across requests](https://hackerone.com/reports/3508701)
   - Program: curl | Upvotes: 8 | Bounty: $0.00 | Type: Use After Free
178. [MQTT: unsigned integer underflow bypasses MAX_MQTT_MESSAGE_SIZE check](https://hackerone.com/reports/3508854)
   - Program: curl | Upvotes: 4 | Bounty: $0.00 | Type: 
179. [integer Overflow in MQTT Protocol Handling Allows Bypassing Message Size Limit](https://hackerone.com/reports/3508500)
   - Program: curl | Upvotes: 5 | Bounty: $0.00 | Type: Integer Overflow
180. [Information Disclosure in API Endpoint /users](https://hackerone.com/reports/3027405)
   - Program: U.S. Dept Of Defense | Upvotes: 27 | Bounty: $0.00 | Type: Information Disclosure
181. [Publicly Accessible CDN Endpoint Exposing XML Metadata (including ETag)](https://hackerone.com/reports/3346375)
   - Program: U.S. Dept Of Defense | Upvotes: 11 | Bounty: $0.00 | Type: Information Disclosure
182. [Create account without auth via response manipulation](https://hackerone.com/reports/2061982)
   - Program: U.S. Dept Of Defense | Upvotes: 38 | Bounty: $0.00 | Type: Business Logic Errors
183. [Information Disclosure via Publicly Accessible Debug Log](https://hackerone.com/reports/3318295)
   - Program: U.S. Dept Of Defense | Upvotes: 14 | Bounty: $0.00 | Type: Information Exposure Through Debug Information
184. [Debug Info disclose](https://hackerone.com/reports/3066992)
   - Program: U.S. Dept Of Defense | Upvotes: 9 | Bounty: $0.00 | Type: Information Exposure Through Debug Information
185. [Reflected XSS Vulnerability in  SSL VPN Endpoint — CVE-2025-0133](https://hackerone.com/reports/3238607)
   - Program: U.S. Dept Of Defense | Upvotes: 15 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
186. [Reflected XSS via user Parameter in /ssl-vpn/getconfig.esp](https://hackerone.com/reports/3205104)
   - Program: U.S. Dept Of Defense | Upvotes: 7 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
187. [Reflected XSS via user Parameter on getconfig.esp Endpoint](https://hackerone.com/reports/3204997)
   - Program: U.S. Dept Of Defense | Upvotes: 8 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
188. [XSS on ███](https://hackerone.com/reports/3053220)
   - Program: U.S. Dept Of Defense | Upvotes: 9 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
189. [Cross-Site Scripting via URL on ████████](https://hackerone.com/reports/3437836)
   - Program: U.S. Dept Of Defense | Upvotes: 11 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
190. [Cross-Site Scripting via 'currentImage' parameter](https://hackerone.com/reports/3136746)
   - Program: U.S. Dept Of Defense | Upvotes: 8 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
191. [Cross-Site Scripting via 'wikitext' parameter](https://hackerone.com/reports/3137212)
   - Program: U.S. Dept Of Defense | Upvotes: 9 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
192. [Cross-Site Scripting (XSS) in ASP.NET via ResolveUrl on ███████](https://hackerone.com/reports/3166582)
   - Program: U.S. Dept Of Defense | Upvotes: 7 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
193. [Cross-Site Scripting (XSS) in ASP.NET via ResolveUrl on ███████](https://hackerone.com/reports/3166581)
   - Program: U.S. Dept Of Defense | Upvotes: 7 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
194. [Cross-Site Scripting (XSS) in ASP.NET via ResolveUrl on ██████████](https://hackerone.com/reports/3166587)
   - Program: U.S. Dept Of Defense | Upvotes: 6 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
195. [Cross-Site Scripting via URL on ███████](https://hackerone.com/reports/3354494)
   - Program: U.S. Dept Of Defense | Upvotes: 7 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
196. [Cross-Site Scripting via URL on ███████](https://hackerone.com/reports/3351408)
   - Program: U.S. Dept Of Defense | Upvotes: 8 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
197. [Cross-Site Scripting via 'RAISED_FUNDS_DESC' parameter](https://hackerone.com/reports/3284389)
   - Program: U.S. Dept Of Defense | Upvotes: 9 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
198. [Cross-Site Scripting via 'autoPlay' parameter](https://hackerone.com/reports/3136754)
   - Program: U.S. Dept Of Defense | Upvotes: 10 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
199. [Cross-Site Scripting via 'description_extra' parameter](https://hackerone.com/reports/3137206)
   - Program: U.S. Dept Of Defense | Upvotes: 9 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
200. [Reflected XSS in `Telerik.ReportViewer.axd` with F5 BIG-IP ASM Bypass on `████`](https://hackerone.com/reports/3135626)
   - Program: U.S. Dept Of Defense | Upvotes: 4 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
