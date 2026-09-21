# HackerOne Public Reports Snapshot

Generated: 2026-09-21T18:53:03.818929+00:00

1. [55: Heap-buffer-overflow read in `curl_formadd_ccsid()` with binary form data](https://hackerone.com/reports/3973245)
   - Program: curl | Upvotes: 5 | Bounty: $0.00 | Type: Out-of-bounds Read
2. [12: SASL DIGEST-MD5 does not validate the server's `rspauth` proof](https://hackerone.com/reports/3972338)
   - Program: curl | Upvotes: 4 | Bounty: $0.00 | Type: Missing Critical Step in Authentication
3. [IMAP connection reuse runs requests in the wrong case-sensitive mailbox](https://hackerone.com/reports/3976342)
   - Program: curl | Upvotes: 6 | Bounty: $0.00 | Type: Improper Handling of Case Sensitivity
4. [27: IMAP custom FETCH listing classification skips literal boundaries, enabling response desynchronization](https://hackerone.com/reports/3971538)
   - Program: curl | Upvotes: 4 | Bounty: $0.00 | Type: 
5. [Conflux-queued zero-length RELAY_END triggers heap out-of-bounds read](https://hackerone.com/reports/3709605)
   - Program: Tor | Upvotes: 12 | Bounty: $0.00 | Type: Out-of-bounds Read
6. [Tor onion service INTRODUCE2 invalid-MAC cells permanently grow service replay cache](https://hackerone.com/reports/3709703)
   - Program: Tor | Upvotes: 10 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
7. [CORS Misconfiguration / Broken Access Control](https://hackerone.com/reports/3930102)
   - Program: Myndr | Upvotes: 9 | Bounty: $0.00 | Type: Improper Access Control - Generic
8. [22:  FTP wildcard matching decodes server-provided filenames, enabling directory traversal](https://hackerone.com/reports/3973143)
   - Program: curl | Upvotes: 11 | Bounty: $0.00 | Type: Path Traversal
9. [Stack Buffer Overflow in mariadb-dump quote_name() Allows Malicious Server to Execute Arbitrary Code on Client](https://hackerone.com/reports/3788482)
   - Program: MariaDB | Upvotes: 29 | Bounty: $0.00 | Type: Stack Overflow
10. [Out-of-bounds read in MariaDB .frm parsing enables RCE via vtable hijacking](https://hackerone.com/reports/3897914)
   - Program: MariaDB | Upvotes: 28 | Bounty: $0.00 | Type: Out-of-bounds Read
11. [49: Cookie-jar save transfers group access to a different GID](https://hackerone.com/reports/3973194)
   - Program: curl | Upvotes: 8 | Bounty: $0.00 | Type: Improper Preservation of Permissions
12. [29: CURLOPT_ISSUERCERT accepts a different-key certificate when issuer metadata collides](https://hackerone.com/reports/3971518)
   - Program: curl | Upvotes: 8 | Bounty: $0.00 | Type: 
13. [08: CVE-2026-7009 fix incomplete for AWS-LC: `--cert-status` bypass on SecTrust path](https://hackerone.com/reports/3973111)
   - Program: curl | Upvotes: 8 | Bounty: $0.00 | Type: Improper Certificate Validation
14. [Apple SecTrust fallback ignores CURLOPT_CRLFILE, letting a revoked cert pass](https://hackerone.com/reports/3993850)
   - Program: curl | Upvotes: 9 | Bounty: $0.00 | Type: 
15. [HTTP Digest nonce reused across an https→http scheme change on the same handle](https://hackerone.com/reports/3993973)
   - Program: curl | Upvotes: 9 | Bounty: $0.00 | Type: 
16. [54: Rejected HTTP/2 push destroys MIME callback state still used by parent (use-after-free)](https://hackerone.com/reports/3973213)
   - Program: curl | Upvotes: 7 | Bounty: $0.00 | Type: Use After Free
17. [57: Heap out-of-bounds read in `curl_easy_escape_ccsid()` / `curl_easy_unescape_ccsid()`](https://hackerone.com/reports/3973219)
   - Program: curl | Upvotes: 4 | Bounty: $0.00 | Type: Out-of-bounds Read
18. [43: HTTP proxy CONNECT header chooses the `-OJ` filename after a redirect](https://hackerone.com/reports/3972293)
   - Program: curl | Upvotes: 5 | Bounty: $0.00 | Type: 
19. [36: HTTP upload resume offset consumed twice after early 307/308 redirect](https://hackerone.com/reports/3971706)
   - Program: curl | Upvotes: 3 | Bounty: $0.00 | Type: 
20. [11: `CURLOPT_FORBID_REUSE` silently lost on multiplexed HTTP/2 connection when the forbidding transfer finishes first](https://hackerone.com/reports/3973121)
   - Program: curl | Upvotes: 3 | Bounty: $0.00 | Type: Authentication Bypass by Primary Weakness
21. [MariaDB GRANT PROXY permits unauthorized authentication changes and administrator account takeover](https://hackerone.com/reports/3876430)
   - Program: MariaDB | Upvotes: 26 | Bounty: $0.00 | Type: Improper Access Control - Generic
22. [MariaDB: heap buffer overflow in ha_tina::chain_append() lets a low-privileged user crash the server via CSV row deletion](https://hackerone.com/reports/3909248)
   - Program: MariaDB | Upvotes: 5 | Bounty: $0.00 | Type: Heap Overflow
23. [KILL authorization trusts the presented login name instead of the authenticated anonymous account](https://hackerone.com/reports/3897588)
   - Program: MariaDB | Upvotes: 8 | Bounty: $0.00 | Type: Incorrect Calculation of Buffer Size
24. [ACL cache collision lets a role inherit privileges from a same-named socket user](https://hackerone.com/reports/3889667)
   - Program: MariaDB | Upvotes: 7 | Bounty: $0.00 | Type: Improper Authentication - Generic
25. [Unauthenticated testing endpoint of notify_push expose internal IP](https://hackerone.com/reports/3513471)
   - Program: Nextcloud | Upvotes: 33 | Bounty: $150.00 | Type: Information Disclosure
26. [Email Enumeration via Password-Protected Share Identity Verification](https://hackerone.com/reports/3507273)
   - Program: Nextcloud | Upvotes: 30 | Bounty: $100.00 | Type: Information Disclosure
27. [Improper Input Validation and Integer Overflow in timeamount parameter of files_retention app](https://hackerone.com/reports/3521639)
   - Program: Nextcloud | Upvotes: 22 | Bounty: $0.00 | Type: Integer Overflow
28. [Missing Duplicate Check allowing Multiple Retention Rules per System Tag](https://hackerone.com/reports/3521646)
   - Program: Nextcloud | Upvotes: 19 | Bounty: $0.00 | Type: Business Logic Errors
29. [Activity app does not verify federated file activity received from remote servers](https://hackerone.com/reports/3534050)
   - Program: Nextcloud | Upvotes: 14 | Bounty: $150.00 | Type: Improper Authentication - Generic
30. [Mail contact autocomplete bypasses administrator-configured user enumeration restrictions and expose member information outside the intended scope](https://hackerone.com/reports/3617729)
   - Program: Nextcloud | Upvotes: 23 | Bounty: $0.00 | Type: Privacy Violation
31. [API token sent to URL dictated by an untrusted project .weblate file](https://hackerone.com/reports/3825141)
   - Program: Weblate | Upvotes: 24 | Bounty: $0.00 | Type: Information Disclosure
32. [Unauthenticated ?q= search query causes exponential pyparsing backtracking under a process-global lock in Weblate](https://hackerone.com/reports/3898281)
   - Program: Weblate | Upvotes: 25 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
33. [Stack Overflow DoS in ST_GeomFromGeoJSON Allows Any Authenticated User to Crash the Entire Server](https://hackerone.com/reports/3769676)
   - Program: MariaDB | Upvotes: 18 | Bounty: $0.00 | Type: Stack Overflow
34. [CVE-2026-82209: domain-scoped PSL domain cookie](https://hackerone.com/reports/3972385)
   - Program: curl | Upvotes: 14 | Bounty: $0.00 | Type: Information Disclosure
35. [CVE-2026-19931: Negotiate ambient user conn reuse](https://hackerone.com/reports/3923520)
   - Program: curl | Upvotes: 11 | Bounty: $0.00 | Type: Authentication Bypass by Primary Weakness
36. [CVE-2026-80229: OpenSSL provider use-after-free](https://hackerone.com/reports/3969255)
   - Program: curl | Upvotes: 7 | Bounty: $0.00 | Type: 
37. [CVE-2026-80230: OpenSSL pinning bypass](https://hackerone.com/reports/3969300)
   - Program: curl | Upvotes: 6 | Bounty: $0.00 | Type: 
38. [CVE-2026-80231: native CA store conn reuse](https://hackerone.com/reports/3969368)
   - Program: curl | Upvotes: 5 | Bounty: $0.00 | Type: 
39. [CVE-2026-82208: wolfSSL CA-cache hit overrides callback](https://hackerone.com/reports/3973090)
   - Program: curl | Upvotes: 3 | Bounty: $0.00 | Type: Improper Certificate Validation
40. [CVE-2026-80255: secure cookie attribute bypass with tab](https://hackerone.com/reports/3972395)
   - Program: curl | Upvotes: 1 | Bounty: $0.00 | Type: Improper Input Validation
41. [CVE-2026-13608: OpenLDAP SASL authentication bypass](https://hackerone.com/reports/3822248)
   - Program: curl | Upvotes: 6 | Bounty: $0.00 | Type: Authentication Bypass by Primary Weakness
42. [CVE-2026-80256: wcurl backslash bypass](https://hackerone.com/reports/3969820)
   - Program: curl | Upvotes: 20 | Bounty: $0.00 | Type: Path Traversal: '.../...//'
43. [SSRF via URL Parser Differential in `normalize_request_url` (wlc)](https://hackerone.com/reports/3887969)
   - Program: Weblate | Upvotes: 37 | Bounty: $0.00 | Type: Server-Side Request Forgery (SSRF)
44. [CVE-2026-18924: HTTP/2 server push UAF](https://hackerone.com/reports/3916059)
   - Program: curl | Upvotes: 13 | Bounty: $0.00 | Type: Use After Free
45. [07: GnuTLS 0-RTT early data bypasses file-backed public-key pin verification](https://hackerone.com/reports/3973098)
   - Program: curl | Upvotes: 8 | Bounty: $0.00 | Type: Information Disclosure
46. [connect.8x8.com: Automation Builder - Input Validation Issue in Workflow Step Outputs](https://hackerone.com/reports/3858504)
   - Program: 8x8 | Upvotes: 31 | Bounty: $1337.00 | Type: External Control of Critical State Data
47. [connect.8x8.com: Deserialization Vulnerability  in Automation Builder via Jint→Newtonsoft serializer coercion (TypeNameHandling)](https://hackerone.com/reports/3861550)
   - Program: 8x8 | Upvotes: 37 | Bounty: $3000.00 | Type: Deserialization of Untrusted Data
48. [Ticket Trick Attack allows access to ████████' workspaces](https://hackerone.com/reports/1534465)
   - Program: Rockstar Games | Upvotes: 48 | Bounty: $0.00 | Type: Improper Access Control - Generic
49. [18:  Explicit IPv6 proxy zone ID silently ignored — proxy credentials sent to wrong interface](https://hackerone.com/reports/3973127)
   - Program: curl | Upvotes: 16 | Bounty: $0.00 | Type: Information Disclosure
50. [33: CONNECT_ONLY raw I/O selects wrong connection after CURLOPT_SHARE detach (incomplete fix for CVE-2020-8231)](https://hackerone.com/reports/3971585)
   - Program: curl | Upvotes: 12 | Bounty: $0.00 | Type: 
51. [41: `main_checkfds()` pipe reuse leaks proxy credentials into HTTPS upload body](https://hackerone.com/reports/3973158)
   - Program: curl | Upvotes: 12 | Bounty: $0.00 | Type: Information Exposure Through Sent Data
52. [06: Incomplete fix for CVE-2026-7009: GCC/SecTrust builds silently discard stapled OCSP responses](https://hackerone.com/reports/3973093)
   - Program: curl | Upvotes: 9 | Bounty: $0.00 | Type: Improper Certificate Validation
53. [**Unauthenticated IDOR allows modification of payment customer billing information**](https://hackerone.com/reports/3869124)
   - Program: Weblate | Upvotes: 67 | Bounty: $0.00 | Type: Insecure Direct Object Reference (IDOR)
54. [50: CMake `HTTP_ONLY` does not disable SSH backends — SCP and SFTP remain usable](https://hackerone.com/reports/3973228)
   - Program: curl | Upvotes: 13 | Bounty: $0.00 | Type: Server-Side Request Forgery (SSRF)
55. [42: `VMS_STS` macro typo (`< 3` vs `<< 3`) turns curl failures into successful OpenVMS conditions](https://hackerone.com/reports/3973169)
   - Program: curl | Upvotes: 11 | Bounty: $0.00 | Type: Improper Check or Handling of Exceptional Conditions
56. [Unauthorized vertical privilege escalation vulnerability found on ibm.com endpoint](https://hackerone.com/reports/3909372)
   - Program: IBM | Upvotes: 21 | Bounty: $0.00 | Type: Improper Access Control - Generic
57. [Author → arbitrary file deletion anywhere on disk (site takeover) via `POST /wp/v2/media/<id>/finalize` poisoning `_wp_attachment_metadata`](https://hackerone.com/reports/3931777)
   - Program: WordPress | Upvotes: 37 | Bounty: $0.00 | Type: Path Traversal
58. [Author → stored XSS in wp-admin: unescaped sub-size filename from attachment metadata breaks out of the `src` attribute in `get_media_item()`](https://hackerone.com/reports/3931771)
   - Program: WordPress | Upvotes: 24 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Stored
59. [Reachable assertion in node:zlib sync API crashes the entire process via spoofed TypedArray byteLength (all 11 *Sync functions affected)](https://hackerone.com/reports/3857258)
   - Program: Node.js | Upvotes: 11 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
60. [HTTP Request Smuggling via Silent Header Truncation in Node.js HTTP Parser](https://hackerone.com/reports/3564941)
   - Program: Node.js | Upvotes: 15 | Bounty: $0.00 | Type: HTTP Request Smuggling
61. [dns.resolveAny() Aborts the Node.js Process When a DNS Response Contains More Than 256 A Records](https://hackerone.com/reports/3795657)
   - Program: Node.js | Upvotes: 10 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
62. [node:sqlite SQLTagStore Iterator Replay Lets Attacker Re-Execute Victim-Bound Writes Indefinitely](https://hackerone.com/reports/3795900)
   - Program: Node.js | Upvotes: 10 | Bounty: $0.00 | Type: Time-of-check Time-of-use (TOCTOU) Race Condition
63. [Re-entrant `nghttp2_session_mem_send()` during `nghttp2_session_mem_recv()` causes heap-use-after-free in Node.js HTTP/2](https://hackerone.com/reports/3833629)
   - Program: Node.js | Upvotes: 15 | Bounty: $0.00 | Type: Use After Free
64. [HTTP/2 retained header blocks evade maxSessionMemory and enable remote memory exhaustion](https://hackerone.com/reports/3846922)
   - Program: Node.js | Upvotes: 11 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
65. [46: `--libcurl` output carries `--insecure` across `--next` boundaries](https://hackerone.com/reports/3972316)
   - Program: curl | Upvotes: 3 | Bounty: $0.00 | Type: 
66. [28: HTTP/3 UDP path ignores CURL_SOCKOPT_ALREADY_CONNECTED, reconnects callback-provided socket](https://hackerone.com/reports/3971496)
   - Program: curl | Upvotes: 3 | Bounty: $0.00 | Type: 
67. [34: `curl_mprintf` reads `double` for documented `long double` conversions — uninitialized value disclosure](https://hackerone.com/reports/3972196)
   - Program: curl | Upvotes: 3 | Bounty: $0.00 | Type: 
68. [--etag-save - truncates append-redirected stdout](https://hackerone.com/reports/3970639)
   - Program: curl | Upvotes: 4 | Bounty: $0.00 | Type: 
69. [Stacked --proto modifiers leave denied protocol enabled](https://hackerone.com/reports/3970650)
   - Program: curl | Upvotes: 3 | Bounty: $0.00 | Type: 
70. [Unbound cross-peer HTTP Digest challenge state](https://hackerone.com/reports/3968729)
   - Program: curl | Upvotes: 13 | Bounty: $0.00 | Type: 
71. [ARG_CLEAR credential scrubbing wipes only UTF-8 copies on Windows Unicode builds](https://hackerone.com/reports/3968431)
   - Program: curl | Upvotes: 4 | Bounty: $0.00 | Type: Information Disclosure
72. [Pre-authentication Stored XSS in Essity Customer-Service Pipeline via ContactApi (reCAPTCHA bypass + no rate limit)](https://hackerone.com/reports/3729501)
   - Program: Essity | Upvotes: 42 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Stored
73. [Critical SQL Injection WDM API (████████)](https://hackerone.com/reports/3778282)
   - Program: Essity | Upvotes: 32 | Bounty: $0.00 | Type: SQL Injection
74. [curl_share TOCTOU > RCE via Curl_llist _dtor Function Pointer Hijack](https://hackerone.com/reports/3955945)
   - Program: curl | Upvotes: 29 | Bounty: $0.00 | Type: Time-of-check Time-of-use (TOCTOU) Race Condition
75. [Hidden/restricted tags can be mutated through synonym ID paths without per-tag authorization](https://hackerone.com/reports/3689633)
   - Program: Discourse | Upvotes: 27 | Bounty: $0.00 | Type: Insecure Direct Object Reference (IDOR)
76. [Add labels to arbitrary issues/prs via Memex Bulk Update to compromise github actions label gating](https://hackerone.com/reports/3527788)
   - Program: GitHub | Upvotes: 41 | Bounty: $0.00 | Type: Insecure Direct Object Reference (IDOR)
77. [TLS session cache case-folds CA paths and bypasses the active trust profile](https://hackerone.com/reports/3966955)
   - Program: curl | Upvotes: 15 | Bounty: $0.00 | Type: Improper Certificate Validation
78. [libcurl Digest/NTLM authentication ignores an explicit Authorization header](https://hackerone.com/reports/3963330)
   - Program: curl | Upvotes: 14 | Bounty: $0.00 | Type: Incorrect Authorization
79. [@jitsi/docker-jitsi-meet: `/colibri-relay-ws/` unsafe nginx regex (OCTO relay configuration)](https://hackerone.com/reports/3889473)
   - Program: 8x8 | Upvotes: 24 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Generic
80. [RTSP CRLF injection in libcurl allows CURLOPT_RTSP_* values to inject commands into independent sessions](https://hackerone.com/reports/3963494)
   - Program: curl | Upvotes: 15 | Bounty: $0.00 | Type: CRLF Injection
81. [wolfSSL backend disables hostname verification when CURLOPT_SSL_VERIFYPEER is 0](https://hackerone.com/reports/3963725)
   - Program: curl | Upvotes: 7 | Bounty: $0.00 | Type: Improper Validation of Certificate with Host Mismatch
82. [URI scheme validation bypass in ActionText `to_markdown` via user-supplied `<action-text-markdown>` marker tag](https://hackerone.com/reports/3727743)
   - Program: Ruby on Rails | Upvotes: 12 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
83. [Path Traversal in Nextcloud Talk Android Exposes User Credentials and Private Data via FileProvider](https://hackerone.com/reports/3696266)
   - Program: Nextcloud | Upvotes: 17 | Bounty: $0.00 | Type: Path Traversal
84. [Domainless COOKIEFILE cookie leaks to unrelated IP-literal hosts](https://hackerone.com/reports/3952619)
   - Program: curl | Upvotes: 31 | Bounty: $0.00 | Type: Information Exposure Through Sent Data
85. [Monero GUI OpenAlias DNSSEC-invalid resolution still writes spoofable address into recipient field](https://hackerone.com/reports/3819475)
   - Program: Monero | Upvotes: 42 | Bounty: $0.00 | Type: 
86. [Background sync cache retains outgoing additional transaction secret keys](https://hackerone.com/reports/3749681)
   - Program: Monero | Upvotes: 1 | Bounty: $0.00 | Type: Information Disclosure
87. [View-only offline transaction creation bypasses the long-payment-ID privacy block](https://hackerone.com/reports/3686283)
   - Program: Monero | Upvotes: 32 | Bounty: $0.00 | Type: Information Disclosure
88. [HTML Injection in Transaction Confirmation Dialog via Address Book Description Enables UI Spoofing Before Fund Transfer](https://hackerone.com/reports/3679471)
   - Program: Monero | Upvotes: 29 | Bounty: $0.00 | Type: Code Injection
89. [Windows installer grants low-privileged users write access to executable P2Pool directory, enabling local code execution](https://hackerone.com/reports/3619409)
   - Program: Monero | Upvotes: 40 | Bounty: $0.00 | Type: Improper Access Control - Generic
90. [monero:// deeplink parsing accepts tx_amount=(all) and can trigger send-all transaction mode](https://hackerone.com/reports/3648638)
   - Program: Monero | Upvotes: 21 | Bounty: $0.00 | Type: Business Logic Errors
91. [Loss of multisig funds through single malicious participant's deliberate deception](https://hackerone.com/reports/3515557)
   - Program: Monero | Upvotes: 12 | Bounty: $0.00 | Type: Business Logic Errors
92. [DDP methods getThreadsList / getThreadMessages leaks private thread content to any authenticated low privilege user (unpatched sibling of #1446767)](https://hackerone.com/reports/3852135)
   - Program: Rocket.Chat | Upvotes: 16 | Bounty: $0.00 | Type: NoSQL Injection
93. [Stored HTML Injection (CWE-79) via Livechat Visitor Name](https://hackerone.com/reports/3872858)
   - Program: Rocket.Chat | Upvotes: 14 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - DOM
94. [Wallet RPC Restricted-Mode Policy Bypass](https://hackerone.com/reports/3620006)
   - Program: Monero | Upvotes: 53 | Bounty: $0.00 | Type: Improper Authentication - Generic
95. [Restricted RPC Policy Bypass on ZMQ JSON-RPC Allows Unauthenticated Remote Admin Actions](https://hackerone.com/reports/3601469)
   - Program: Monero | Upvotes: 39 | Bounty: $0.00 | Type: Improper Authentication - Generic
96. [TaskProcessing callback authorization bypass allows ex-members to post as Assistant Talk Bot](https://hackerone.com/reports/3799010)
   - Program: Nextcloud | Upvotes: 71 | Bounty: $0.00 | Type: Insecure Direct Object Reference (IDOR)
97. [Windows SSPI connection-pool probe can reuse a connection under the wrong user](https://hackerone.com/reports/3938185)
   - Program: curl | Upvotes: 37 | Bounty: $0.00 | Type: Authentication Bypass by Spoofing
98. [libcurl cache updates follow symlinks and truncate their targets](https://hackerone.com/reports/3938220)
   - Program: curl | Upvotes: 21 | Bounty: $0.00 | Type: Time-of-check Time-of-use (TOCTOU) Race Condition
99. [Cookie jar load skips public suffix check on PSL builds](https://hackerone.com/reports/3920276)
   - Program: curl | Upvotes: 20 | Bounty: $0.00 | Type: Information Exposure Through Sent Data
100. [Debug Deep Link Abuse Allows Repeated Forced Logout and Application Disruption](https://hackerone.com/reports/3829030)
   - Program: Yelp | Upvotes: 51 | Bounty: $0.00 | Type: Violation of Secure Design Principles
101. [JaaS SIP Gateway Authorization Bypass](https://hackerone.com/reports/3837634)
   - Program: 8x8 | Upvotes: 64 | Bounty: $500.00 | Type: Missing Authorization
102. [Myndr CORS Misconfiguration](https://hackerone.com/reports/3930957)
   - Program: Myndr | Upvotes: 36 | Bounty: $0.00 | Type: Improper Access Control - Generic
103. [Adding phone number to profile By OTP brute forcing](https://hackerone.com/reports/3265780)
   - Program: CoinMate.io | Upvotes: 109 | Bounty: $100.00 | Type: Insecure Storage of Sensitive Information
104. [URL API: triple-slash parses path segment as hostname](https://hackerone.com/reports/3923212)
   - Program: curl | Upvotes: 27 | Bounty: $0.00 | Type: Use of Incorrectly-Resolved Name or Reference
105. [[Wii U/3DS/Switch] Improper bounds check in StationURL in all NEX clients leading to remote crash/RCE](https://hackerone.com/reports/2551512)
   - Program: Nintendo | Upvotes: 41 | Bounty: $0.00 | Type: Stack Overflow
106. [Unauthenticated RCE in Taskcluster web-server via GraphQL filter argument (sift $where)](https://hackerone.com/reports/3782701)
   - Program: Mozilla | Upvotes: 331 | Bounty: $12000.00 | Type: Code Injection
107. [curl Missing Sec-WebSocket-Accept Verification Enables MITM WebSocket Session Hijacking](https://hackerone.com/reports/3917775)
   - Program: curl | Upvotes: 37 | Bounty: $0.00 | Type: Man-in-the-Middle
108. [`check_reserve_proof` counts duplicate entries: one output can inflate `total`](https://hackerone.com/reports/3699522)
   - Program: Monero | Upvotes: 42 | Bounty: $0.00 | Type: Business Logic Errors
109. [`check_reserve_proof` sums RingCT ECDH amounts without checking the output commitment](https://hackerone.com/reports/3698862)
   - Program: Monero | Upvotes: 37 | Bounty: $0.00 | Type: Missing Required Cryptographic Step
110. [wallet-rpc crash via malformed /gettransactions response (empty txs → vector::front() in check_tx_key / check_tx_proof)](https://hackerone.com/reports/3693636)
   - Program: Monero | Upvotes: 44 | Bounty: $0.00 | Type: NULL Pointer Dereference
111. [SpendProofV1 txid-substitution: get_spend_proof/check_spend_proof do not verify returned transaction hash](https://hackerone.com/reports/3700036)
   - Program: Monero | Upvotes: 28 | Bounty: $0.00 | Type: Missing Required Cryptographic Step
112. [wallet-rpc describe_transfer uses real_output_in_tx_index instead of real_output: cold-wallet pre-sign review shows wrong ring member](https://hackerone.com/reports/3723315)
   - Program: Monero | Upvotes: 19 | Bounty: $0.00 | Type: Array Index Underflow
113. [`set_daemon` wallet-rpc silently ignores `ssl_allowed_fingerprints` → pinning bypassed, wallet↔daemon MITM](https://hackerone.com/reports/3686259)
   - Program: Monero | Upvotes: 6 | Bounty: $0.00 | Type: Improper Certificate Validation
114. [`relay_tx` wallet-rpc skips `--restricted-rpc` guard and lets any caller corrupt wallet state via attacker-controlled `pending_tx`](https://hackerone.com/reports/3687543)
   - Program: Monero | Upvotes: 20 | Bounty: $0.00 | Type: Improper Access Control - Generic
115. [Heap use-after-free (write) in mev_forget_socket() via reentrant curl_easy_pause() — incomplete fix for CVE-2026-9080](https://hackerone.com/reports/3911968)
   - Program: curl | Upvotes: 10 | Bounty: $0.00 | Type: Use After Free
116. [GitHub Retired UsernameTakeover From  [aws/████████]](https://hackerone.com/reports/3478646)
   - Program: AWS VDP | Upvotes: 43 | Bounty: $0.00 | Type: Inclusion of Functionality from Untrusted Control Sphere
117. [Unauthenticated Path Traversal (LFI) via /custom-sounds/ when CustomSounds uses FileSystem storage](https://hackerone.com/reports/3514640)
   - Program: Rocket.Chat | Upvotes: 46 | Bounty: $0.00 | Type: Path Traversal
118. [SMTP CRLF injection in custom SMTP recipient operand allows additional SMTP commands after authentication](https://hackerone.com/reports/3911605)
   - Program: curl | Upvotes: 19 | Bounty: $0.00 | Type: CRLF Injection
119. [Unauthenticated team "income/payments" export ignores donor privacy settings (hide_giving, hide_from_lists) and uses frozen visibility, exposing donat](https://hackerone.com/reports/3878586)
   - Program: Liberapay | Upvotes: 68 | Bounty: $100.00 | Type: 
120. [HTTP Request Smuggling via Connection: close<TAB> in Node.js llhttp parser](https://hackerone.com/reports/3723248)
   - Program: Node.js | Upvotes: 49 | Bounty: $0.00 | Type: HTTP Request Smuggling
121. [Stored XSS in nameserver field on account settings page](https://hackerone.com/reports/3644182)
   - Program: Tucows (VDP) | Upvotes: 53 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Stored
122. [Stored XSS via SVG Upload — check_content() Blocklist Bypass & 256-Byte Scan Limit (Self-Propagating Worm)](https://hackerone.com/reports/3606773)
   - Program: phpBB | Upvotes: 53 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Stored
123. [Permission Model bypass: process.report writes (and overwrites) files outside --allow-fs-write paths](https://hackerone.com/reports/3815767)
   - Program: Node.js | Upvotes: 35 | Bounty: $0.00 | Type: Improper Access Control - Generic
124. [Active Storage Vips Transformer Missing validate_transformation — CVE-2025-24293 Incomplete Fix](https://hackerone.com/reports/3553340)
   - Program: Ruby on Rails | Upvotes: 30 | Bounty: $0.00 | Type: Path Traversal
125. [HTTPS Agent TLS session reuse skips hostname verification across identity policies (incomplete fix of CVE-2026-48934)](https://hackerone.com/reports/3812439)
   - Program: Node.js | Upvotes: 37 | Bounty: $0.00 | Type: Exploiting Incorrectly Configured SSL/TLS
126. [GitHub scoped user to server tokens can escape their installation](https://hackerone.com/reports/3638909)
   - Program: GitHub | Upvotes: 78 | Bounty: $0.00 | Type: Improper Access Control - Generic
127. [Permission Model: --allow-fs-read/--allow-fs-write radix-tree prefix-boundary over-grant](https://hackerone.com/reports/3761342)
   - Program: Node.js | Upvotes: 32 | Bounty: $0.00 | Type: Improper Access Control - Generic
128. [`exportReportPdf` mutation shows internal Activity](https://hackerone.com/reports/3577216)
   - Program: HackerOne | Upvotes: 84 | Bounty: $0.00 | Type: 
129. [HTTPS Agent PFX object-array key collision allows mTLS client identity reuse across different per-request certificates](https://hackerone.com/reports/3816840)
   - Program: Node.js | Upvotes: 24 | Bounty: $0.00 | Type: Improper Authentication - Generic
130. [Permission Model Bypass: `trace_events.createTracing().enable()` Writes Trace Logs Outside `--allow-fs-write`](https://hackerone.com/reports/3838601)
   - Program: Node.js | Upvotes: 21 | Bounty: $0.00 | Type: Improper Access Control - Generic
131. [Unauthenticated SSRF in Voxtelesys integration ('checkUrlForSsrf' Bypass via DNS rebinding)](https://hackerone.com/reports/3473145)
   - Program: Rocket.Chat | Upvotes: 28 | Bounty: $0.00 | Type: Server-Side Request Forgery (SSRF)
132. [Sandbox User Can Inject Rogue CA Certificate into OS Trust Store via Sudo-Allowed deploy-certificates.sh](https://hackerone.com/reports/3633146)
   - Program: AWS VDP | Upvotes: 16 | Bounty: $0.00 | Type: Improper Certificate Validation
133. [Non-Production API Endpoints for the Amazon Cloudwatch Fails to Log to CloudTrail Resulting in Silent Permission Enumeration](https://hackerone.com/reports/3775702)
   - Program: AWS VDP | Upvotes: 19 | Bounty: $0.00 | Type: Insufficient Logging
134. [Authentication Bypass via XML Signature Wrapping in SAML SSO](https://hackerone.com/reports/3827674)
   - Program: Rocket.Chat | Upvotes: 38 | Bounty: $0.00 | Type: Improper Authentication - Generic
135. [ZMQ RPC Log Injection and Untrusted Payload Persistence](https://hackerone.com/reports/3621606)
   - Program: Monero | Upvotes: 30 | Bounty: $0.00 | Type: CRLF Injection
136. [AWS *.a2z.com | Unauthenticated Clickhouse UI : Database access + SSRF](https://hackerone.com/reports/3809407)
   - Program: AWS VDP | Upvotes: 53 | Bounty: $0.00 | Type: Authentication Bypass
137. [GitHub user to server tokens can create issues in any public repository](https://hackerone.com/reports/3641229)
   - Program: GitHub | Upvotes: 60 | Bounty: $0.00 | Type: Improper Access Control - Generic
138. [connect.8x8.com/api/v1: JWT Algorithm Confusion Vulnerability](https://hackerone.com/reports/3800870)
   - Program: 8x8 | Upvotes: 105 | Bounty: $1337.00 | Type: Improper Verification of Cryptographic Signature
139. [OAuth redirect uri validation bypass for :proxima_first_party_sync apps](https://hackerone.com/reports/3588801)
   - Program: GitHub | Upvotes: 77 | Bounty: $0.00 | Type: Open Redirect
140. [Restricted RPC leaks alternative block hashes via /get_alt_blocks_hashes](https://hackerone.com/reports/3738727)
   - Program: Monero | Upvotes: 51 | Bounty: $0.00 | Type: Improper Access Control - Generic
141. [Stored XSS in Rocket.Chat HTML File Export — Unauthenticated Entry via LiveChat](https://hackerone.com/reports/3779690)
   - Program: Rocket.Chat | Upvotes: 95 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Stored
142. [Able to bypass authorization logic and gain more access then intended](https://hackerone.com/reports/3713965)
   - Program: GitHub | Upvotes: 103 | Bounty: $0.00 | Type: 
143. [Bedrock AgentCore Starter Toolkit Creates Gateway IAM Roles Without Confused Deputy Protections](https://hackerone.com/reports/3632577)
   - Program: AWS VDP | Upvotes: 47 | Bounty: $0.00 | Type: Incorrect Permission Assignment for Critical Resource
144. [Stored XSS on Trix Editor version latest (2.1.16) - Sanitizer Bypass](https://hackerone.com/reports/3581911)
   - Program: Basecamp | Upvotes: 84 | Bounty: $337.00 | Type: Cross-site Scripting (XSS) - Stored
145. [bedrock-mantle.api.aws accepts Bedrock API keys outside the IAM Deny, CloudTrail signal, and invocation logging AWS publishes for Bedrock keys](https://hackerone.com/reports/3702072)
   - Program: AWS VDP | Upvotes: 44 | Bounty: $0.00 | Type: Insecure Default Initialization of Resource
146. [SELECT ... INTO OUTFILE does not enforce the FILE WRITE privilege  unprivileged arbitrary file write on the   server](https://hackerone.com/reports/3780695)
   - Program: SingleStore | Upvotes: 50 | Bounty: $0.00 | Type: Missing Authorization
147. [Kiro IDE Stores Auth Tokens with World-Readable Permissions (0644)](https://hackerone.com/reports/3630605)
   - Program: AWS VDP | Upvotes: 54 | Bounty: $0.00 | Type: Incorrect Default Permissions
148. [OS Command Injection in `aws-cdk-lib` NodejsFunction via Unsanitized `OsCommand` Helper (Supply Chain RCE)](https://hackerone.com/reports/3637898)
   - Program: AWS VDP | Upvotes: 111 | Bounty: $0.00 | Type: OS Command Injection
149. [Any installed app can force immediate logout and persistent DOS of authenticated Basecamp sessions via unprotected exported StartActivity](https://hackerone.com/reports/3764217)
   - Program: Basecamp | Upvotes: 103 | Bounty: $0.00 | Type: Improper Access Control - Generic
150. [admin.shopify.com: Shopify Flow continues sending internal emails to a configured recipient after the staff author is removed](https://hackerone.com/reports/3628961)
   - Program: Shopify | Upvotes: 76 | Bounty: $0.00 | Type: 
151. [Non-Production API Endpoints for the Amazon S3 Tables Service Fails to Log to CloudTrail Resulting in Silent Permission Enumeration](https://hackerone.com/reports/3780277)
   - Program: AWS VDP | Upvotes: 68 | Bounty: $0.00 | Type: Insufficient Logging
152. [jitsi-meet: Prosody/Jigasi missing header whitelist in mod_filter_iq_rayo allows arbitrary SIP header injection and Caller ID spoofing](https://hackerone.com/reports/3789570)
   - Program: 8x8 | Upvotes: 71 | Bounty: $100.00 | Type: Improper Input Validation
153. [jitsi-call-analytics: Unauthenticated arbitrary file write via path traversal in `/api/v1/uploads/analyze`](https://hackerone.com/reports/3485343)
   - Program: 8x8 | Upvotes: 66 | Bounty: $100.00 | Type: Path Traversal
154. [Yelp for Business: locked Email field silently editable via API](https://hackerone.com/reports/3766455)
   - Program: Yelp | Upvotes: 75 | Bounty: $0.00 | Type: Client-Side Enforcement of Server-Side Security
155. [Splatoon 3 In-Match Integrity Bypass via Consensus Reflection Attack on Unordered Peer Submission](https://hackerone.com/reports/3559522)
   - Program: Nintendo | Upvotes: 60 | Bounty: $0.00 | Type: Client-Side Enforcement of Server-Side Security
156. [[Splatoon 3] Kick other players with NplnLogin message](https://hackerone.com/reports/3813932)
   - Program: Nintendo | Upvotes: 35 | Bounty: $0.00 | Type: Improper Access Control - Generic
157. [Exceeding the maximum number of spaces allowed by exploiting a Race Condition in the Workspace creation process](https://hackerone.com/reports/3295500)
   - Program: SingleStore | Upvotes: 34 | Bounty: $0.00 | Type: Business Logic Errors
158. [Insecure Direct Object Reference (IDOR) allows creating folders.](https://hackerone.com/reports/3353057)
   - Program: SingleStore | Upvotes: 36 | Bounty: $0.00 | Type: Insecure Direct Object Reference (IDOR)
159. [Delete any folder for any user within the organization](https://hackerone.com/reports/3353035)
   - Program: SingleStore | Upvotes: 34 | Bounty: $0.00 | Type: Insecure Direct Object Reference (IDOR)
160. [Privilege Escalation – Access to the Alert Subscribers page for users with low privileges](https://hackerone.com/reports/3353000)
   - Program: SingleStore | Upvotes: 26 | Bounty: $0.00 | Type: Privilege Escalation
161. [Improper Input Validation — HTTP Response Parser Unconditionally Accepts Bare CR in Status Line](https://hackerone.com/reports/3648681)
   - Program: Node.js | Upvotes: 29 | Bounty: $0.00 | Type: HTTP Request Smuggling
162. [heap-use-after-free in curl_easy_cleanup() called from callback](https://hackerone.com/reports/3833577)
   - Program: curl | Upvotes: 13 | Bounty: $0.00 | Type: Use After Free
163. [setopt(VERIFYPEER) from callback bypasses TLS verify on connection reuse](https://hackerone.com/reports/3831432)
   - Program: curl | Upvotes: 7 | Bounty: $0.00 | Type: 
164. [ssh_config_matches is dead code: unauthorized SSH key reuse](https://hackerone.com/reports/3826843)
   - Program: curl | Upvotes: 11 | Bounty: $0.00 | Type: Authentication Bypass by Primary Weakness
165. [CURLSHOPT_UNSHARE race can cause UAF in shared SSL session cache during HTTPS transfer](https://hackerone.com/reports/3831345)
   - Program: curl | Upvotes: 3 | Bounty: $0.00 | Type: Use After Free
166. [libcurl upload read callbacks miss recursive API guard, allowing prohibited multi API reentry and ASAN-confirmed UAF](https://hackerone.com/reports/3832393)
   - Program: curl | Upvotes: 2 | Bounty: $0.00 | Type: 
167. [Denial of Service (DoS) Vulnerability in Drafts Creation Endpoint](https://hackerone.com/reports/3400140)
   - Program: Discourse | Upvotes: 93 | Bounty: $1024.00 | Type: Uncontrolled Resource Consumption
168. [Inverted ternary in peerlist_manager::filter() allows unlimited whitelist entries per host via different ports](https://hackerone.com/reports/3547349)
   - Program: Monero | Upvotes: 18 | Bounty: $0.00 | Type: 
169. [Remote node DOS](https://hackerone.com/reports/876530)
   - Program: Monero | Upvotes: 24 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
170. [UAF read in mev_pollset_diff() trace path after curl_easy_pause() in socket callback](https://hackerone.com/reports/3824303)
   - Program: curl | Upvotes: 19 | Bounty: $0.00 | Type: Use After Free
171. [Use-after-free in `mev_forget_socket` when `curl_easy_pause()` is called from a `CURL_POLL_REMOVE` socket callback (incomplete fix of CVE-2026-9080)](https://hackerone.com/reports/3823985)
   - Program: curl | Upvotes: 13 | Bounty: $0.00 | Type: Use After Free
172. [mbedTLS / wolfSSL / rustls backends silently skip hostname verification when CURLOPT_SSL_VERIFYPEER=0](https://hackerone.com/reports/3826199)
   - Program: curl | Upvotes: 18 | Bounty: $0.00 | Type: Improper Validation of Certificate with Host Mismatch
173. [CURLOPT_HAPROXY_CLIENT_IP lacks input validation, enabling HAProxy PROXY protocol injection](https://hackerone.com/reports/3823932)
   - Program: curl | Upvotes: 13 | Bounty: $0.00 | Type: CRLF Injection
174. [PHP code injection in delivery-limitation `logical` validation bypass - XML-RPC setChannelTargeting](https://hackerone.com/reports/3781492)
   - Program: Revive Adserver | Upvotes: 45 | Bounty: $0.00 | Type: Code Injection
175. [XML‑RPC login leak exposes valid session ID enabling unauthorized API access](https://hackerone.com/reports/3783738)
   - Program: Revive Adserver | Upvotes: 28 | Bounty: $0.00 | Type: Improper Access Control - Generic
176. [Reflected XSS via unsanitised refresh parameter in zone invocation tag](https://hackerone.com/reports/3780806)
   - Program: Revive Adserver | Upvotes: 28 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
177. [PHP code injection in delivery-limitation `logical` validation bypass](https://hackerone.com/reports/3780854)
   - Program: Revive Adserver | Upvotes: 33 | Bounty: $0.00 | Type: Code Injection
178. [Stored XSS in maintenance tools via unescaped entity names](https://hackerone.com/reports/3781311)
   - Program: Revive Adserver | Upvotes: 24 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Stored
179. [CSRF in zone‑include.php allows unauthorized banner and campaign linking](https://hackerone.com/reports/3781691)
   - Program: Revive Adserver | Upvotes: 19 | Bounty: $0.00 | Type: Cross-Site Request Forgery (CSRF)
180. [Missing ownership validation allows cross‑manager tracker–campaign linking](https://hackerone.com/reports/3780709)
   - Program: Revive Adserver | Upvotes: 22 | Bounty: $0.00 | Type: Insecure Direct Object Reference (IDOR)
181. [Reflected XSS in stats‑video.php via improperly encoded URL parameters](https://hackerone.com/reports/3793243)
   - Program: Revive Adserver | Upvotes: 10 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
182. [HTTP Response Queue Poisoning via TOCTOU Race Condition in `http.Agent`](https://hackerone.com/reports/3582376)
   - Program: Node.js | Upvotes: 11 | Bounty: $0.00 | Type: Time-of-check Time-of-use (TOCTOU) Race Condition
183. [Unix domain socket server bypasses --permission network restrictions (incomplete CVE-2026-21636 fix)](https://hackerone.com/reports/3618831)
   - Program: Node.js | Upvotes: 8 | Bounty: $0.00 | Type: Improper Access Control - Generic
184. [Node.js unicode dot separator handling can lead to tls wildcard-depth authentication bypass due to resolver and verifier hostname normalization mismat](https://hackerone.com/reports/3688064)
   - Program: Node.js | Upvotes: 18 | Bounty: $0.00 | Type: Improper Handling of Unicode Encoding
185. [Uppercase sni context matching can lead to mtls authorization bypass due to case-sensitive hostname matching](https://hackerone.com/reports/3656869)
   - Program: Node.js | Upvotes: 7 | Bounty: $0.00 | Type: Improper Access Control - Generic
186. [TLS host identity verification bypass via session reuse with different servername leads to unauthorized connections](https://hackerone.com/reports/3649802)
   - Program: Node.js | Upvotes: 5 | Bounty: $0.00 | Type: Exploiting Incorrectly Configured SSL/TLS
187. [Permission Model bypass via FileHandle.utimes() in the promises API](https://hackerone.com/reports/3625987)
   - Program: Node.js | Upvotes: 4 | Bounty: $0.00 | Type: Incorrect Default Permissions
188. [Proxy credentials leaked in ERR_PROXY_TUNNEL error message](https://hackerone.com/reports/3720313)
   - Program: Node.js | Upvotes: 4 | Bounty: $0.00 | Type: Privacy Violation
189. [Unbounded memory growth in `node:http2` clients via attacker-controlled ORIGIN frames](https://hackerone.com/reports/3676863)
   - Program: Node.js | Upvotes: 4 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
190. [Embedded-nul hostnames can lead to silent authority rebinding due to c-string truncation in resolver bindings](https://hackerone.com/reports/3656716)
   - Program: Node.js | Upvotes: 4 | Bounty: $0.00 | Type: Improper Access Control - Generic
191. [Node.js WebCrypto AES Integer Overflow Leads to Remote Process Abort (DoS)](https://hackerone.com/reports/3760016)
   - Program: Node.js | Upvotes: 13 | Bounty: $0.00 | Type: Integer Overflow
192. [HTTPS proxy connection reuse lets one easy handle inherit another handle's mTLS-authenticated proxy session](https://hackerone.com/reports/3735180)
   - Program: curl | Upvotes: 6 | Bounty: $0.00 | Type: Exposure of Data Element to Wrong Session
193. [CVE-2026-11564: Native CA trust persist](https://hackerone.com/reports/3788984)
   - Program: curl | Upvotes: 7 | Bounty: $0.00 | Type: 
194. [CVE-2026-12064: proto-default skips SSH verification](https://hackerone.com/reports/3797526)
   - Program: curl | Upvotes: 8 | Bounty: $0.00 | Type: Improper Certificate Validation
195. [CVE-2026-11586: WS Auto-PONG memory exhaustion](https://hackerone.com/reports/3788931)
   - Program: curl | Upvotes: 6 | Bounty: $0.00 | Type: Allocation of Resources Without Limits or Throttling
196. [CVE-2026-11352: QUIC zero-length UDP datagrams busy-loop](https://hackerone.com/reports/3783438)
   - Program: curl | Upvotes: 7 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
197. [CVE-2026-10536: HTTP/2 stream-dependency tree UAF](https://hackerone.com/reports/3751697)
   - Program: curl | Upvotes: 5 | Bounty: $0.00 | Type: Buffer Over-read
198. [CVE-2026-8924: trailing dot domain super cookie](https://hackerone.com/reports/3733905)
   - Program: curl | Upvotes: 1 | Bounty: $0.00 | Type: Use of Incorrectly-Resolved Name or Reference
199. [CVE-2026-9547: SSH improper host validation](https://hackerone.com/reports/3751712)
   - Program: curl | Upvotes: 2 | Bounty: $0.00 | Type: Reusing a Nonce, Key Pair in Encryption
200. [CVE-2026-9546: sending old referer](https://hackerone.com/reports/3754343)
   - Program: curl | Upvotes: 3 | Bounty: $0.00 | Type: Use After Free
