# HackerOne Public Reports Snapshot

Generated: 2026-11-10T20:34:13.887545+00:00

1. [Unescaped consent-prompt renderer (HTML()) enables concealed-approval OS command injection in strands-agents/tools use_computer — RCE](https://hackerone.com/reports/4077800)
   - Program: AWS VDP | Upvotes: 13 | Bounty: $0.00 | Type: OS Command Injection
2. [Unauthenticated Disclosure of Private, Draft, and Password-Protected Post Content via Core Read-Permission Bypass in SCF Reference Fields](https://hackerone.com/reports/4152553)
   - Program: WordPress | Upvotes: 27 | Bounty: $0.00 | Type: Information Disclosure
3. [WordCamp Meta gpre: password-protected event RSVP list readable without password via /gpre/v1/.../rsvp-responses](https://hackerone.com/reports/4029867)
   - Program: WordPress | Upvotes: 23 | Bounty: $0.00 | Type: Improper Access Control - Generic
4. [wordpress.org Rosetta: invite stores unvalidated role — Editor can assign site Administrator despite editable_roles](https://hackerone.com/reports/3942522)
   - Program: WordPress | Upvotes: 24 | Bounty: $0.00 | Type: Improper Access Control - Generic
5. [Instamojo CampTix: fail-open MAC + webhook Credit without binding payment to order](https://hackerone.com/reports/3941626)
   - Program: WordPress | Upvotes: 17 | Bounty: $0.00 | Type: Improper Access Control - Generic
6. [Unauthenticated private CSV export of Meetup organizer PII via broken authz check in WordCamp Reports](https://hackerone.com/reports/3871816)
   - Program: WordPress | Upvotes: 16 | Bounty: $0.00 | Type: Improper Access Control - Generic
7. [CPU-based Denial of Service in translation-finder via O(N²) per-result wildcard mask matching](https://hackerone.com/reports/4088592)
   - Program: Weblate | Upvotes: 13 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
8. [Connector/C TLS auth-switch bypass exposes plaintext password on hostname verification failure](https://hackerone.com/reports/3896617)
   - Program: MariaDB | Upvotes: 12 | Bounty: $0.00 | Type: Improper Certificate Validation
9. [Connector/C Out-of-bounds read from unterminated GSSAPI SPN in `parse_server_packet()`](https://hackerone.com/reports/3896684)
   - Program: MariaDB | Upvotes: 6 | Bounty: $0.00 | Type: Out-of-bounds Read
10. [Connector/ODBC: MADB_Stmt::ArrayOffset is not reset when an exception unwinds out of MADB_StmtExecute, so the next paramset reads out of bounds](https://hackerone.com/reports/3920647)
   - Program: MariaDB | Upvotes: 6 | Bounty: $0.00 | Type: Out-of-bounds Read
11. [Connector/ODBC: SqlwcsOctetLen sizes UTF-16 with a byte-oriented helper, reading past the caller's buffer and sending client memory to the server](https://hackerone.com/reports/3920633)
   - Program: MariaDB | Upvotes: 7 | Bounty: $0.00 | Type: Out-of-bounds Read
12. [r2dbc-mariadb: server message accepted with no command in flight desynchronises the connection and serves one user's rows to another](https://hackerone.com/reports/3920629)
   - Program: MariaDB | Upvotes: 3 | Bounty: $0.00 | Type: Information Disclosure
13. [Connector/ODBC injects unquoted column names into positioned DELETE and UPDATE via MADB_DynStrGetWhere](https://hackerone.com/reports/3891779)
   - Program: MariaDB | Upvotes: 2 | Bounty: $0.00 | Type: SQL Injection
14. [Connector/ODBC SQLGetDescRec treats descriptor handle as statement handle, heap OOB write on every call](https://hackerone.com/reports/3891337)
   - Program: MariaDB | Upvotes: 3 | Bounty: $0.00 | Type: Type Confusion
15. [Stack buffer overflow in 9 of 10 Connector/ODBC catalog functions via unbounded name](https://hackerone.com/reports/3891319)
   - Program: MariaDB | Upvotes: 3 | Bounty: $0.00 | Type: Stack Overflow
16. [Connector/C++ ignores allowMultiQueries and injects savepoint names into SQL](https://hackerone.com/reports/3890329)
   - Program: MariaDB | Upvotes: 4 | Bounty: $0.00 | Type: SQL Injection
17. [Connector/C++ aborts client process on server session-tracking packet via std::stoi](https://hackerone.com/reports/3890352)
   - Program: MariaDB | Upvotes: 2 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
18. [Connector/C++ string escaper re-escapes its own output, enabling SQL injection](https://hackerone.com/reports/3890289)
   - Program: MariaDB | Upvotes: 3 | Bounty: $0.00 | Type: SQL Injection
19. [Unauthenticated access to Checkout Blocks employee-only endpoints exposed merchant metadata](https://hackerone.com/reports/3954327)
   - Program: Shopify | Upvotes: 33 | Bounty: $3100.00 | Type: Missing Authentication for Critical Function
20. [`Vary` cache-key conflation of absent and empty request fields](https://hackerone.com/reports/4062511)
   - Program: Django | Upvotes: 7 | Bounty: $0.00 | Type: 
21. [Re-entrant curl_easy_pause UAF in cw-pause](https://hackerone.com/reports/4166602)
   - Program: curl | Upvotes: 6 | Bounty: $0.00 | Type: Use After Free
22. [`monero-wallet-rpc::rescan_spent` accepts daemon-supplied spent-status from an untrusted daemon, enabling ring-intersection attack on transactions](https://hackerone.com/reports/3719670)
   - Program: Monero | Upvotes: 21 | Bounty: $0.00 | Type: Information Disclosure
23. [CampTix [camptix_private]: the view token is derived from the requester's own IP, so naming any attendee's e-mail unlocks the gated content](https://hackerone.com/reports/4043537)
   - Program: WordPress | Upvotes: 36 | Bounty: $0.00 | Type: Improper Authentication - Generic
24. [wordpress.org/openverse/: unauthenticated open redirect — `str_replace()`'s 4th arg is a count, not a limit; bypasses WordPress.org SSO allow-list](https://hackerone.com/reports/3933198)
   - Program: WordPress | Upvotes: 31 | Bounty: $0.00 | Type: Open Redirect
25. [launchpad.37signals.com OAuth AS issues victim-bound credential to unverified attacker redirect → full CIA triad on Basecamp API](https://hackerone.com/reports/3955956)
   - Program: Basecamp | Upvotes: 49 | Bounty: $0.00 | Type: Improper Authentication - Generic
26. [Cross-account webhook takeover: PUT and DELETE on /<account>/webhooks/<id>.json reach another account's webhook](https://hackerone.com/reports/3979217)
   - Program: Basecamp | Upvotes: 34 | Bounty: $0.00 | Type: Improper Authentication - Generic
27. [A third-party Basecamp OAuth token mints a full launchpad web session through GET /my/login_option](https://hackerone.com/reports/3999856)
   - Program: Basecamp | Upvotes: 33 | Bounty: $0.00 | Type: Improper Access Control - Generic
28. [Incomplete VCS metadata exclusion: `.svn` / `.bzr` bypass CVE-2026-61792 due to missing `VCS_METADATA_DIRS` entries.](https://hackerone.com/reports/4037976)
   - Program: Weblate | Upvotes: 21 | Bounty: $0.00 | Type: Path Traversal
29. [wlc: Project-wide download fails part-way and leaves stale archives on disk; filesystem errors surface as raw Python tracebacks.](https://hackerone.com/reports/4040149)
   - Program: Weblate | Upvotes: 14 | Bounty: $0.00 | Type: Information Exposure Through an Error Message
30. [Translation discovery crashes on crafted filenames (regex substitution injection)](https://hackerone.com/reports/4044441)
   - Program: Weblate | Upvotes: 11 | Bounty: $0.00 | Type: Use of Externally-Controlled Format String
31. [Revoked deployment collaborator regains access to private comments after active collaborator interaction](https://hackerone.com/reports/3852102)
   - Program: Vercel | Upvotes: 55 | Bounty: $1026.00 | Type: Access Control Check Implemented After Asset is Accessed
32. [Monero IPv6 /128 tracking bypasses per-IP limit, enables remote OOM](https://hackerone.com/reports/3816330)
   - Program: Monero | Upvotes: 23 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
33. [Cross-account XSS on app.basecamp.com: oEmbed option injection chained through Turbo defeats the CSP nonce](https://hackerone.com/reports/3981292)
   - Program: Basecamp | Upvotes: 27 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Generic
34. [Launchpad file read leaks production keys](https://hackerone.com/reports/3962925)
   - Program: Basecamp | Upvotes: 55 | Bounty: $9337.00 | Type: Path Traversal
35. [FederationController::remoteWopiToken() returns full Wopi entity without token type validation](https://hackerone.com/reports/3568116)
   - Program: Nextcloud | Upvotes: 17 | Bounty: $0.00 | Type: Improper Access Control - Generic
36. [SSRF on Nextcloud Whiteboard Application via Recordings to Unauthorised Access to Whiteboards](https://hackerone.com/reports/3576823)
   - Program: Nextcloud | Upvotes: 17 | Bounty: $250.00 | Type: Server-Side Request Forgery (SSRF)
37. [Tables application does not respect sharing limitations set by admin](https://hackerone.com/reports/3642236)
   - Program: Nextcloud | Upvotes: 6 | Bounty: $0.00 | Type: Improper Access Control - Generic
38. [Users with read-only access to a Nextcloud Table can enumerate its share recipients via the Tables API](https://hackerone.com/reports/3524971)
   - Program: Nextcloud | Upvotes: 12 | Bounty: $0.00 | Type: Information Disclosure
39. [Unauthorized users can enumerate internal team resources via the Teams API when a team is visible to everyone](https://hackerone.com/reports/3511955)
   - Program: Nextcloud | Upvotes: 9 | Bounty: $0.00 | Type: Improper Access Control - Generic
40. [Unauthorised access with hidden public link creation when sharing to a Team External Member](https://hackerone.com/reports/3625932)
   - Program: Nextcloud | Upvotes: 11 | Bounty: $100.00 | Type: Privilege Escalation
41. [Files Confidential tagging can be bypassed with # in filename](https://hackerone.com/reports/3682163)
   - Program: Nextcloud | Upvotes: 4 | Bounty: $0.00 | Type: Improper Access Control - Generic
42. [Public shares remain accessible via alternate endpoints after owner account is disabled](https://hackerone.com/reports/3620539)
   - Program: Nextcloud | Upvotes: 6 | Bounty: $270.00 | Type: Improper Access Control - Generic
43. [Unauthenticated Persistent Denial-of-Service via Federated Share Injection](https://hackerone.com/reports/3679640)
   - Program: Nextcloud | Upvotes: 3 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
44. [No password confirmation required when using apptoken on sensitive endpoint](https://hackerone.com/reports/3566607)
   - Program: Nextcloud | Upvotes: 2 | Bounty: $0.00 | Type: Improper Privilege Management
45. [Incomplete IDN hostname check on the transfer path can lead to credential disclosure to an unintended host](https://hackerone.com/reports/4147581)
   - Program: curl | Upvotes: 1 | Bounty: $0.00 | Type: 
46. [Permission Model filesystem over-grant via wildcard radix lookup](https://hackerone.com/reports/3996423)
   - Program: Node.js | Upvotes: 6 | Bounty: $0.00 | Type: Improper Access Control - Generic
47. [netrc credentials leaked to a cross-host redirect target on the Basic auth path (not covered by redirect credential protections)](https://hackerone.com/reports/4125043)
   - Program: curl | Upvotes: 4 | Bounty: $0.00 | Type: Insufficiently Protected Credentials
48. [wolfSSL TLS sessions retain native-CA trust after the application narrows trust](https://hackerone.com/reports/4122227)
   - Program: curl | Upvotes: 5 | Bounty: $0.00 | Type: Improper Certificate Validation
49. [OpenSSL `--cert-status` accepts indefinitely stale GOOD OCSP staples](https://hackerone.com/reports/4125601)
   - Program: curl | Upvotes: 2 | Bounty: $0.00 | Type: Improper Check for Certificate Revocation
50. [GnuTLS + Apple SecTrust discards authenticated OCSP failure](https://hackerone.com/reports/4124276)
   - Program: curl | Upvotes: 2 | Bounty: $0.00 | Type: Improper Certificate Validation
51. [OpenSSL+Apple SecTrust: SecTrust accepts certificates that the app's CURLOPT_SSL_CTX_FUNCTION trust store or verify callback rejected](https://hackerone.com/reports/4123304)
   - Program: curl | Upvotes: 3 | Bounty: $0.00 | Type: Improper Certificate Validation
52. [Cross-protocol redirect to imap:// or smtp:// uploads the -F/MIMEPOST form and the custom Authorization/Cookie headers to the redirect target](https://hackerone.com/reports/4123474)
   - Program: curl | Upvotes: 1 | Bounty: $0.00 | Type: Information Exposure Through Sent Data
53. [A disabled account's API key still works on BMO's Mojolicious /rest/ routes, including for security-group bugs filed after the disable](https://hackerone.com/reports/4000084)
   - Program: Mozilla | Upvotes: 32 | Bounty: $4000.00 | Type: Improper Authentication - Generic
54. [OpenSSL provider OSSL_LIB_CTX used after free via the connection shutdown list (CVE-2026-80229 fix incomplete)](https://hackerone.com/reports/4118643)
   - Program: curl | Upvotes: 3 | Bounty: $0.00 | Type: Use After Free
55. [FTP authentication options leak to a cross-origin FTP redirect with unrestricted auth disabled](https://hackerone.com/reports/4105790)
   - Program: curl | Upvotes: 1 | Bounty: $0.00 | Type: Insufficiently Protected Credentials
56. [14: HSTS cache import silently drops a longer-lived child beneath an includeSubDomains parent](https://hackerone.com/reports/3973124)
   - Program: curl | Upvotes: 0 | Bounty: $0.00 | Type: Cleartext Transmission of Sensitive Information
57. [20: HTAB before `Secure` attribute silently drops the Secure cookie flag](https://hackerone.com/reports/3971551)
   - Program: curl | Upvotes: 1 | Bounty: $0.00 | Type: 
58. [Windows SSPI connection-pool probe can reuse a connection under the wrong user](https://hackerone.com/reports/3938190)
   - Program: curl | Upvotes: 3 | Bounty: $0.00 | Type: Authentication Bypass by Spoofing
59. [Derived cookie Path aborts cookie jar loading in curl 8.23.0](https://hackerone.com/reports/4127231)
   - Program: curl | Upvotes: 2 | Bounty: $0.00 | Type: Improper Input Validation
60. [server filename with control characters printed to terminal (`-J`)](https://hackerone.com/reports/4130124)
   - Program: curl | Upvotes: 2 | Bounty: $0.00 | Type: Improper Neutralization of Escape, Meta, or Control Sequences
61. [CVE-2026-115529: Schannel TLS auto client session resumption](https://hackerone.com/reports/4136767)
   - Program: curl | Upvotes: 1 | Bounty: $0.00 | Type: Improper Authentication - Generic
62. [CVE-2026-111954: upload reader failed redirect UAF](https://hackerone.com/reports/4123190)
   - Program: curl | Upvotes: 1 | Bounty: $0.00 | Type: Use After Free
63. [CVE-2026-111953: GnuTLS SecTrust OCSP staple bypass](https://hackerone.com/reports/4122300)
   - Program: curl | Upvotes: 2 | Bounty: $0.00 | Type: Improper Certificate Validation
64. [CVE-2026-111950: TLS session cache diff scheme reuse](https://hackerone.com/reports/4122175)
   - Program: curl | Upvotes: 1 | Bounty: $0.00 | Type: Incorrect Comparison
65. [CVE-2026-111484: OpenSSL with SecTrust accepts bad OCSP staples](https://hackerone.com/reports/4118610)
   - Program: curl | Upvotes: 4 | Bounty: $0.00 | Type: Improper Certificate Validation
66. [CVE-2026-111482: libssh2 knownhosts prefix match](https://hackerone.com/reports/4112709)
   - Program: curl | Upvotes: 1 | Bounty: $0.00 | Type: Partial String Comparison
67. [CVE-2026-111481: server-set cookie still aborts cookie jar](https://hackerone.com/reports/4112912)
   - Program: curl | Upvotes: 1 | Bounty: $0.00 | Type: Improper Input Validation
68. [CVE-2026-111480: pause UAF from within callback](https://hackerone.com/reports/4102061)
   - Program: curl | Upvotes: 1 | Bounty: $0.00 | Type: Use After Free
69. [CVE-2026-111952: OpenSSL provider use-after-free again](https://hackerone.com/reports/4122239)
   - Program: curl | Upvotes: 1 | Bounty: $0.00 | Type: Use After Free
70. [CVE-2026-111878: OpenSSL provider UAF on TLS shutdown](https://hackerone.com/reports/4116527)
   - Program: curl | Upvotes: 2 | Bounty: $0.00 | Type: Use After Free
71. [CVE-2026-111951: curl -OJ truncate without filename](https://hackerone.com/reports/4124849)
   - Program: curl | Upvotes: 4 | Bounty: $0.00 | Type: External Control of File Name or Path
72. [CVE-2026-115528: wolfSSL TLS connect without cert](https://hackerone.com/reports/4128428)
   - Program: curl | Upvotes: 4 | Bounty: $0.00 | Type: Improper Certificate Validation
73. [CVE-2026-111483: GnuTLS accepts non-successful OCSP staples](https://hackerone.com/reports/4116076)
   - Program: curl | Upvotes: 3 | Bounty: $0.00 | Type: Improper Check for Certificate Revocation
74. [Arbitrary `/tmp` read in  discourse via `convert_heif!` decoder-confusion (regression of 4bf3bf6786)](https://hackerone.com/reports/3738834)
   - Program: Discourse | Upvotes: 4 | Bounty: $0.00 | Type: Information Disclosure
75. [Code injection allows unprivileged local attacker to execute arbitrary code in Nextcloud's OAuth/web renderer process](https://hackerone.com/reports/3772818)
   - Program: Nextcloud | Upvotes: 11 | Bounty: $0.00 | Type: Code Injection
76. [Null Dereference in X509ToObject](https://hackerone.com/reports/3824331)
   - Program: Node.js | Upvotes: 22 | Bounty: $0.00 | Type: NULL Pointer Dereference
77. [Permission Model bypass with fs.realpathSync](https://hackerone.com/reports/3838675)
   - Program: Node.js | Upvotes: 15 | Bounty: $0.00 | Type: Improper Access Control - Generic
78. [Improper certificate validation for non-canonical IPv4 hostnames allows DNS SANs to authenticate IP endpoints](https://hackerone.com/reports/3962304)
   - Program: Node.js | Upvotes: 13 | Bounty: $0.00 | Type: Improper Certificate Validation
79. [TLS certificate hostname bypass when the IP is written fullwidth digits](https://hackerone.com/reports/4038287)
   - Program: Node.js | Upvotes: 29 | Bounty: $0.00 | Type: Improper Certificate Validation
80. [Keep-alive socket process a response that was written before the request was sent](https://hackerone.com/reports/4038361)
   - Program: Node.js | Upvotes: 15 | Bounty: $0.00 | Type: Time-of-check Time-of-use (TOCTOU) Race Condition
81. [TLS certificate hostname bypass when the host loosely resolves to an IP address](https://hackerone.com/reports/4006744)
   - Program: Node.js | Upvotes: 24 | Bounty: $0.00 | Type: Improper Certificate Validation
82. [CURL_NETRC_REQUIRED sends the URL password when the .netrc file has no matching entry](https://hackerone.com/reports/4137523)
   - Program: curl | Upvotes: 6 | Bounty: $0.00 | Type: Expected Behavior Violation
83. [dns.resolve truncates names containing NUL char](https://hackerone.com/reports/4038342)
   - Program: Node.js | Upvotes: 18 | Bounty: $0.00 | Type: Improper Access Control - Generic
84. [Heap-use-after-free in libcurl's multi event machinery (curl_multi_remove_handle() from a socket callback nested under a notify callback)](https://hackerone.com/reports/4135291)
   - Program: curl | Upvotes: 9 | Bounty: $0.00 | Type: Use After Free
85. [--cert-status with OpenSSL accepts a stapled OCSP response of any age when it lacks nextUpdate (revoked certificate keeps passing)](https://hackerone.com/reports/4135826)
   - Program: curl | Upvotes: 6 | Bounty: $0.00 | Type: Improper Check for Certificate Revocation
86. [curl EXPIRE_SHUTDOWN timer never armed for silent servers: connection-shutdown timeout bypass in cshutdn (event-driven mode)](https://hackerone.com/reports/4125065)
   - Program: curl | Upvotes: 5 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
87. [passive FTPS data connection handshake blocks curl_multi_perform() with no timeout (regression in 8.19.0)](https://hackerone.com/reports/4122567)
   - Program: curl | Upvotes: 4 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
88. [Pinned public key check passes for a key the server does not hold with the wolfSSL backend](https://hackerone.com/reports/4128701)
   - Program: curl | Upvotes: 8 | Bounty: $0.00 | Type: Improper Certificate Validation
89. [A server response that answers nothing is used as the next transfer's reply — and with IMAP, a fully compliant server does this by accident](https://hackerone.com/reports/4131903)
   - Program: curl | Upvotes: 5 | Bounty: $0.00 | Type: 
90. [IDN decoding inserts authority delimiters and can redirect proxy CONNECT to a different host](https://hackerone.com/reports/4129950)
   - Program: curl | Upvotes: 12 | Bounty: $0.00 | Type: Server-Side Request Forgery (SSRF)
91. [WordPress 7.1 Media Processing Race Enables Persistent PHP File Write and Author-to-RCE](https://hackerone.com/reports/3923967)
   - Program: WordPress | Upvotes: 37 | Bounty: $0.00 | Type: Code Injection
92. [Large-site Quick Edit reparses a Contributor display name into active HTML](https://hackerone.com/reports/3878399)
   - Program: WordPress | Upvotes: 20 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - DOM
93. [Cross-room signaling injection enabling unauthorized force-mute](https://hackerone.com/reports/3636758)
   - Program: Nextcloud | Upvotes: 12 | Bounty: $0.00 | Type: Improper Authentication - Generic
94. [Redirect to imap/pop3/smtp (SASL) or sftp/scp (libssh) authenticates to the attacker's host with the user's ambient Kerberos credentials](https://hackerone.com/reports/4123571)
   - Program: curl | Upvotes: 9 | Bounty: $0.00 | Type: Information Exposure Through Sent Data
95. [CVE-2026-11586 fix is incomplete: auto-PONG memory grows without limit through curl_ws_recv() (CONNECT_ONLY)](https://hackerone.com/reports/4123050)
   - Program: curl | Upvotes: 6 | Bounty: $0.00 | Type: Allocation of Resources Without Limits or Throttling
96. [POP3: data after the end-of-body terminator is written into the retrieved message](https://hackerone.com/reports/4132132)
   - Program: curl | Upvotes: 4 | Bounty: $0.00 | Type: Acceptance of Extraneous Untrusted Data With Trusted Data
97. [curl reuses an HTTPS connection when a response is already buffered in the TLS stack](https://hackerone.com/reports/4128703)
   - Program: curl | Upvotes: 5 | Bounty: $0.00 | Type: Acceptance of Extraneous Untrusted Data With Trusted Data
98. [TLS session cache ignores CURLOPT_SSL_CTX_FUNCTION identity and resumes one client's session for another](https://hackerone.com/reports/4129638)
   - Program: curl | Upvotes: 5 | Bounty: $0.00 | Type: Improper Certificate Validation
99. [HSTS cache file: three trailing dots silently disable HSTS for that host](https://hackerone.com/reports/4129642)
   - Program: curl | Upvotes: 8 | Bounty: $0.00 | Type: Improper Certificate Validation
100. [Application Data Hiding via Invalid `iconName` Causing Frontend Crash in Nextcloud Tables](https://hackerone.com/reports/3508852)
   - Program: Nextcloud | Upvotes: 25 | Bounty: $0.00 | Type: Business Logic Errors
101. [Deck app: Invalid tag color is accepted by API and breaks frontend UI](https://hackerone.com/reports/3485178)
   - Program: Nextcloud | Upvotes: 21 | Bounty: $0.00 | Type: Business Logic Errors
102. [Ordinary HEY user can make HEY originate authenticated mail from attacker-selected @hey.com  addresses](https://hackerone.com/reports/4035023)
   - Program: Basecamp | Upvotes: 44 | Bounty: $0.00 | Type: Improper Access Control - Generic
103. [TLS session cache key omits native_ca_store: a session validated with CURLSSLOPT_NATIVE_CA can be resumed by a transfer that disabled it (incomplete f](https://hackerone.com/reports/4123646)
   - Program: curl | Upvotes: 6 | Bounty: $0.00 | Type: Improper Certificate Validation
104. [CURLOPT_PROXYHEADER is not part of the HTTP-proxy connection reuse key: a second CONNECT-tunnel transfer silently reuses the first tunnel's Proxy-Auth](https://hackerone.com/reports/4124549)
   - Program: curl | Upvotes: 5 | Bounty: $0.00 | Type: Improper Authentication - Generic
105. [WebSocket send queue use-after-free during nested curl_ws_send()](https://hackerone.com/reports/4124722)
   - Program: curl | Upvotes: 2 | Bounty: $0.00 | Type: Use After Free
106. [SSH (SCP/SFTP) host-key verification is skipped on connection reuse — a pinned/known_hosts transfer silently reuses a previously-unverified connection](https://hackerone.com/reports/4124583)
   - Program: curl | Upvotes: 3 | Bounty: $0.00 | Type: Improper Validation of Certificate with Host Mismatch
107. [wolfSSL Backend Silently Ignores --cert-status (OCSP Stapling Bypass)](https://hackerone.com/reports/4127399)
   - Program: curl | Upvotes: 1 | Bounty: $0.00 | Type: Improper Certificate Validation
108. [Symlink-following truncation of arbitrary files in `Curl_fopen()` when saving cookie jars, HSTS, or alt-svc caches](https://hackerone.com/reports/4125257)
   - Program: curl | Upvotes: 2 | Bounty: $0.00 | Type: Insecure Temporary File
109. [WebSocket decoder use-after-free when curl_easy_pause() unpauses from a debug callback](https://hackerone.com/reports/4123749)
   - Program: curl | Upvotes: 8 | Bounty: $0.00 | Type: Use After Free
110. [SSH host-key policy is missing from the connection-reuse tuple: strict pins and knownhosts are silently skipped on reused SFTP/SCP connections](https://hackerone.com/reports/4126768)
   - Program: curl | Upvotes: 5 | Bounty: $0.00 | Type: Authentication Bypass by Primary Weakness
111. [IBC2 Entry Points Skip SetupContractCost - Systematic Gas Underpricing](https://hackerone.com/reports/3547607)
   - Program: Cosmos | Upvotes: 9 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
112. [SCP upload with --crlf sends more bytes than the size declared to the server (same class curl refused for IMAP CVE-2026-87864 and RTSP)](https://hackerone.com/reports/4123654)
   - Program: curl | Upvotes: 5 | Bounty: $0.00 | Type: CRLF Injection
113. [curl CONNECT response header colon-check bypass in cf-h1-proxy single_header — proxy authentication bypass via injected HTTP/1.x status line](https://hackerone.com/reports/4053116)
   - Program: curl | Upvotes: 9 | Bounty: $0.00 | Type: Improper Authentication - Generic
114. [urlapi: CURLUPART_HOST accepts text after an IPv6 zone ip and URL round trip changes the host](https://hackerone.com/reports/4127756)
   - Program: curl | Upvotes: 5 | Bounty: $0.00 | Type: Improper Input Validation
115. [RTSP ANNOUNCE/SET_PARAMETER upload with --use-ascii / CURLOPT_TRANSFERTEXT sends more body bytes than the declared Content-Length (incomplete fix of e](https://hackerone.com/reports/4124486)
   - Program: curl | Upvotes: 5 | Bounty: $0.00 | Type: CRLF Injection
116. [curl RTSP connection reuse routes response headers to the RTP callback (rtsp_conn state machine not reset between sessions)](https://hackerone.com/reports/4121685)
   - Program: curl | Upvotes: 6 | Bounty: $0.00 | Type: 
117. [libcurl TLS shorter-retry mismatch discloses client heap memory during cancelled IMAPS upload](https://hackerone.com/reports/4105853)
   - Program: curl | Upvotes: 3 | Bounty: $0.00 | Type: Out-of-bounds Read
118. [libcurl shared-HSTS-cache race leads to use-after-free with attacker-controlled function-pointer call](https://hackerone.com/reports/4122039)
   - Program: curl | Upvotes: 8 | Bounty: $0.00 | Type: Use After Free
119. [SMTP header injection via C-escape `\r` in the recipient display name](https://hackerone.com/reports/3913007)
   - Program: Nextcloud | Upvotes: 23 | Bounty: $0.00 | Type: Buffer Over-read
120. [CRLF injection in the HTTP request-line via `CURLOPT_REQUEST_TARGET` (`--request-target`)](https://hackerone.com/reports/4121689)
   - Program: curl | Upvotes: 6 | Bounty: $0.00 | Type: CRLF Injection
121. [CRLF injection in the RTSP request-line and Transport header via `CURLOPT_RTSP_STREAM_URI` and `CURLOPT_RTSP_TRANSPORT`](https://hackerone.com/reports/4121675)
   - Program: curl | Upvotes: 6 | Bounty: $0.00 | Type: CRLF Injection
122. [libcurl RTSP `CURLOPT_CRLF` conversion allows a request body to become a second RTSP request](https://hackerone.com/reports/4113412)
   - Program: curl | Upvotes: 16 | Bounty: $0.00 | Type: Improper Input Validation
123. [Explicit NO_PROXY /0 CIDR rules fail to bypass HTTP proxy for IP-literal requests](https://hackerone.com/reports/4114965)
   - Program: curl | Upvotes: 13 | Bounty: $0.00 | Type: Information Exposure Through Sent Data
124. [Unauthenticated go-httpbin servers : Leads to Cookie Tossing on *.aws.dev and Open Redirect](https://hackerone.com/reports/3966599)
   - Program: AWS VDP | Upvotes: 32 | Bounty: $0.00 | Type: Missing Authentication for Critical Function
125. [SQL Injection vulnerability found on IBM.com subdomain](https://hackerone.com/reports/3730301)
   - Program: IBM | Upvotes: 36 | Bounty: $0.00 | Type: SQL Injection
126. [Memory exhaustion (DoS) via unbounded file read in `EncodingDiscovery.detect_encoding()`](https://hackerone.com/reports/4028616)
   - Program: Weblate | Upvotes: 24 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
127. [TFTP accepts a first response from an IP other than the requested server](https://hackerone.com/reports/4103651)
   - Program: curl | Upvotes: 10 | Bounty: $0.00 | Type: Man-in-the-Middle
128. [HTTP/1.1 connection reuse returns unsolicited server data as the next request's response (regression in 8.22.0)](https://hackerone.com/reports/4098761)
   - Program: curl | Upvotes: 16 | Bounty: $0.00 | Type: HTTP Request Smuggling
129. [Open redirect on app.hey.com bypasses HEY desktop's internal-origin allowlist and loads attacker content inside a HEY BrowserWindow](https://hackerone.com/reports/3972760)
   - Program: Basecamp | Upvotes: 33 | Bounty: $0.00 | Type: Open Redirect
130. [Burp Suite OpenAPI Event Log HTML injection triggers Windows SMB authentication](https://hackerone.com/reports/3972558)
   - Program: PortSwigger Web Security | Upvotes: 58 | Bounty: $1000.00 | Type: 
131. [IMAP custom FETCH literals can spoof tagged responses and desynchronize reused connections](https://hackerone.com/reports/4021854)
   - Program: curl | Upvotes: 6 | Bounty: $0.00 | Type: 
132. [One Strict-Transport-Security response header empties the victim's entire HSTS store, silently,](https://hackerone.com/reports/4007917)
   - Program: curl | Upvotes: 5 | Bounty: $0.00 | Type: Cleartext Transmission of Sensitive Information
133. [Cross-origin redirect reuses a pooled Negotiate-authenticated connection from an unrelated transfer](https://hackerone.com/reports/3981716)
   - Program: curl | Upvotes: 3 | Bounty: $0.00 | Type: 
134. [An organization admin can create an attacker-controlled organization owner via the gem transfer flow](https://hackerone.com/reports/3938927)
   - Program: RubyGems | Upvotes: 27 | Bounty: $0.00 | Type: Improper Access Control - Generic
135. [[Switch] Remote stack buffer overflow in the LDN/LP2P DHCP server leads to control-flow hijack](https://hackerone.com/reports/3770768)
   - Program: Nintendo | Upvotes: 35 | Bounty: $0.00 | Type: Stack Overflow
136. [Retry-independent time-condition HTTP/2 UAF](https://hackerone.com/reports/4033108)
   - Program: curl | Upvotes: 6 | Bounty: $0.00 | Type: Use After Free
137. [Unauthenticated self-registration on ████████ grants full access to internal supplier procurement portal and vendor data](https://hackerone.com/reports/4071064)
   - Program: Essity | Upvotes: 29 | Bounty: $0.00 | Type: Missing Authentication for Critical Function
138. [Uncaught RecursionError crash in translation-finder (deep directory tree DoS)](https://hackerone.com/reports/4022462)
   - Program: Weblate | Upvotes: 16 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
139. [Stored XSS on the public Pontoon dashboards: the latest-activity tooltip re-parses a contributor's account address as HTML](https://hackerone.com/reports/3988961)
   - Program: Mozilla | Upvotes: 61 | Bounty: $3000.00 | Type: Cross-site Scripting (XSS) - Stored
140. [CVE-2026-107928: info leak uploading over WebSockets with GnuTLS](https://hackerone.com/reports/4099194)
   - Program: curl | Upvotes: 7 | Bounty: $0.00 | Type: Buffer Over-read
141. [CVE-2026-107929: local interface connection reuse mixup](https://hackerone.com/reports/4099618)
   - Program: curl | Upvotes: 5 | Bounty: $0.00 | Type: Exposure of Data Element to Wrong Session
142. [CVE-2026-86413: Negotiate credentials sent to redirected origin](https://hackerone.com/reports/3993549)
   - Program: curl | Upvotes: 4 | Bounty: $0.00 | Type: 
143. [CVE-2026-92391: curl_mime_free stack overflow by recursion](https://hackerone.com/reports/4024222)
   - Program: curl | Upvotes: 2 | Bounty: $0.00 | Type: 
144. [CVE-2026-92386: server-set cookie aborts cookie jar load](https://hackerone.com/reports/4021979)
   - Program: curl | Upvotes: 0 | Bounty: $0.00 | Type: 
145. [CVE-2026-92387: never-ending loop via server response omission](https://hackerone.com/reports/4022003)
   - Program: curl | Upvotes: 0 | Bounty: $0.00 | Type: 
146. [CVE-2026-87863: HSTS response erases persisted entries](https://hackerone.com/reports/3972373)
   - Program: curl | Upvotes: 3 | Bounty: $0.00 | Type: Time-of-check Time-of-use (TOCTOU) Race Condition
147. [CVE-2026-87864: IMAP APPEND plus CRLF conversion command injection](https://hackerone.com/reports/3972403)
   - Program: curl | Upvotes: 0 | Bounty: $0.00 | Type: CRLF Injection
148. [CVE-2026-86415: auto client cert connection reuse mixup](https://hackerone.com/reports/3993870)
   - Program: curl | Upvotes: 2 | Bounty: $0.00 | Type: 
149. [CVE-2026-87862: HSTS cache import drops longer-lived child](https://hackerone.com/reports/3972357)
   - Program: curl | Upvotes: 0 | Bounty: $0.00 | Type: Cleartext Transmission of Sensitive Information
150. [CVE-2026-86414: leaking host credentials to HTTP proxy](https://hackerone.com/reports/3993566)
   - Program: curl | Upvotes: 0 | Bounty: $0.00 | Type: 
151. [CVE-2026-86412: server-set cookie erases cookie jar](https://hackerone.com/reports/3973201)
   - Program: curl | Upvotes: 0 | Bounty: $0.00 | Type: Improper Check or Handling of Exceptional Conditions
152. [CVE-2026-86411: FTP connection reuse inherits client-certificate](https://hackerone.com/reports/3973190)
   - Program: curl | Upvotes: 1 | Bounty: $0.00 | Type: Authentication Bypass by Primary Weakness
153. [CVE-2026-92389: TFTP direction confusion](https://hackerone.com/reports/4022568)
   - Program: curl | Upvotes: 0 | Bounty: $0.00 | Type: 
154. [CVE-2026-86409: stale SigV4 headers sent unintended](https://hackerone.com/reports/3973135)
   - Program: curl | Upvotes: 0 | Bounty: $0.00 | Type: Information Disclosure
155. [CVE-2026-86410:  redirect to SFTP or SCP bypasses host verification](https://hackerone.com/reports/3973176)
   - Program: curl | Upvotes: 0 | Bounty: $0.00 | Type: Improper Validation of Certificate with Host Mismatch
156. [CVE-2026-92390: -J no-clobber guarantee bypassed with 103 early hints](https://hackerone.com/reports/4023192)
   - Program: curl | Upvotes: 0 | Bounty: $0.00 | Type: 
157. [CVE-2026-92388: FTP wildcard write callback mixup](https://hackerone.com/reports/4022070)
   - Program: curl | Upvotes: 0 | Bounty: $0.00 | Type: 
158. [CVE-2026-87866: wolfSSL public-key pinning bypass](https://hackerone.com/reports/3989514)
   - Program: curl | Upvotes: 2 | Bounty: $0.00 | Type: Improper Certificate Validation
159. [CVE-2026-87865: knownhost callback mismatches key as missing](https://hackerone.com/reports/3975408)
   - Program: curl | Upvotes: 0 | Bounty: $0.00 | Type: Improper Validation of Certificate with Host Mismatch
160. [CVE-2026-94266: password leak in CURLINFO_EFFECTIVE_URL](https://hackerone.com/reports/4041053)
   - Program: curl | Upvotes: 1 | Bounty: $0.00 | Type: 
161. [CVE-2026-94265: Authorization: Negotiate sent to foreign origin](https://hackerone.com/reports/4040551)
   - Program: curl | Upvotes: 1 | Bounty: $0.00 | Type: 
162. [CVE-2026-87861: cross-origin reuse of a Negotiate connection](https://hackerone.com/reports/3972094)
   - Program: curl | Upvotes: 1 | Bounty: $0.00 | Type: Improper Authentication - Generic
163. [CVE-2026-92392: HTTP/2 upload Use-After-Free](https://hackerone.com/reports/4030333)
   - Program: curl | Upvotes: 9 | Bounty: $0.00 | Type: Use After Free
164. [RCE in AWS Amplify CLI via Prototype Chain Traversal in amplify-velocity-template](https://hackerone.com/reports/3897236)
   - Program: AWS VDP | Upvotes: 25 | Bounty: $0.00 | Type: Code Injection
165. [Stack Buffer Overflow in MariaDB CONNECT storage engine when reading DOUBLE columns from TABLE_TYPE=DOS tables](https://hackerone.com/reports/3910393)
   - Program: MariaDB | Upvotes: 16 | Bounty: $0.00 | Type: Stack Overflow
166. [SQL Injection found on ibm.com subdomain](https://hackerone.com/reports/3662095)
   - Program: IBM | Upvotes: 33 | Bounty: $0.00 | Type: SQL Injection
167. [Connector/ODBC: malicious server's long version string wraps size_t PrefixLen via negative _snprintf return, causing heap out-of-bounds write](https://hackerone.com/reports/3871977)
   - Program: MariaDB | Upvotes: 7 | Bounty: $0.00 | Type: Memory Corruption - Generic
168. [Connector/C++: heap out-of-bounds read when malicious server field length exceeds declared column length in binary result path](https://hackerone.com/reports/3872248)
   - Program: MariaDB | Upvotes: 6 | Bounty: $0.00 | Type: Out-of-bounds Read
169. [r2dbc-mariadb Parsec auth: server-controlled PBKDF2 iteration count causes CPU-exhaustion DoS ( regression from b7766de )](https://hackerone.com/reports/3871740)
   - Program: MariaDB | Upvotes: 6 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
170. [Unauthenticated disclosure of private and hidden forum content in bbPress via the WordPress core REST single-item endpoint](https://hackerone.com/reports/3801107)
   - Program: WordPress | Upvotes: 23 | Bounty: $0.00 | Type: Improper Access Control - Generic
171. [Server crash (stack-overflow DoS) via unbounded recursion in MariaDB WKB GEOMETRYCOLLECTION parser](https://hackerone.com/reports/3896507)
   - Program: MariaDB | Upvotes: 18 | Bounty: $0.00 | Type: 
172. [ActionText `to_markdown` still allows `javascript:` links in kramdown via Rails-generated table cells after PR #58754](https://hackerone.com/reports/4082665)
   - Program: Ruby on Rails | Upvotes: 15 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
173. [Information Disclosure - Unauthen Leak Private Content](https://hackerone.com/reports/4053546)
   - Program: WordPress | Upvotes: 27 | Bounty: $0.00 | Type: Information Disclosure
174. [Full Admin Takeover of R3 Limited's JFrog Artifactory - 292 Users, Corda Enterprise & CBDC Supply Chain Compromised](https://hackerone.com/reports/3994056)
   - Program: R3 | Upvotes: 91 | Bounty: $0.00 | Type: Improper Authentication - Generic
175. [Cookie attribute truncation in curl drops Secure/HttpOnly protections](https://hackerone.com/reports/4093443)
   - Program: curl | Upvotes: 17 | Bounty: $0.00 | Type: Information Exposure Through Sent Data
176. [curl tool: --hsts is ignored for a schemeless URL starting with a slash under --proto-default http](https://hackerone.com/reports/4063328)
   - Program: curl | Upvotes: 13 | Bounty: $0.00 | Type: Cleartext Transmission of Sensitive Information
177. [HackerOne Code: a live password reset token reaches Datadog RUM, and the same session records the account it unlocks](https://hackerone.com/reports/4071670)
   - Program: HackerOne | Upvotes: 45 | Bounty: $200.00 | Type: Insufficiently Protected Credentials
178. [MariaDB HandlerSocket Improper Request Field-Count Validation Causes Server Crash](https://hackerone.com/reports/3867363)
   - Program: MariaDB | Upvotes: 23 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
179. [MariaDB Low-Privilege User Can Exhaust Memory Through a Formatting Function and Crash the Service](https://hackerone.com/reports/3867358)
   - Program: MariaDB | Upvotes: 16 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
180. [DROP PACKAGE leaves PACKAGE BODY grant in mysql.procs_priv causing privilege escalation](https://hackerone.com/reports/3908943)
   - Program: MariaDB | Upvotes: 19 | Bounty: $0.00 | Type: Improper Access Control - Generic
181. [Pre-authentication `size_t` integer underflow → out-of-bounds read / server crash in MariaDB `caching_sha2_password` (auth_mysql_sha2) via an RSA-OAEP](https://hackerone.com/reports/3781201)
   - Program: MariaDB | Upvotes: 14 | Bounty: $0.00 | Type: Integer Underflow
182. [Missing FILE-privilege enforcement in CONNECT file UDFs allows server-side file read and write](https://hackerone.com/reports/3836021)
   - Program: MariaDB | Upvotes: 14 | Bounty: $0.00 | Type: Improper Access Control - Generic
183. [DATA / INDEX DIRECTORY Abuse](https://hackerone.com/reports/3849025)
   - Program: MariaDB | Upvotes: 8 | Bounty: $0.00 | Type: 
184. [`SHOW [CREATE|GRANTS] ...` / `mariadb-dump` Unescaped SQL Generation](https://hackerone.com/reports/3848978)
   - Program: MariaDB | Upvotes: 5 | Bounty: $0.00 | Type: SQL Injection
185. [Privilege escalation via user controlled usernames / roles and views](https://hackerone.com/reports/3880451)
   - Program: MariaDB | Upvotes: 6 | Bounty: $0.00 | Type: 
186. [#mysql50# legacy alias / internal table collisions](https://hackerone.com/reports/3849051)
   - Program: MariaDB | Upvotes: 5 | Bounty: $0.00 | Type: 
187. [#mysql50# legacy alias / stale table cache identity mismatch](https://hackerone.com/reports/3849040)
   - Program: MariaDB | Upvotes: 5 | Bounty: $0.00 | Type: 
188. [Low-privilege RCE in MariaDB: SYS_REFCURSOR cursor-array use-after-free chained with an ST_Area heap over-read](https://hackerone.com/reports/3856148)
   - Program: MariaDB | Upvotes: 14 | Bounty: $0.00 | Type: Use After Free
189. [Heap Use-After-Free in Materialized_cursor::open via SYS_REFCURSOR Array Reallocation](https://hackerone.com/reports/3915935)
   - Program: MariaDB | Upvotes: 6 | Bounty: $0.00 | Type: Use After Free
190. [Possible DoS in NumberHelpers](https://hackerone.com/reports/2814774)
   - Program: Ruby on Rails | Upvotes: 18 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
191. [libcurl: Secure=1 cookie flag bypasses the 8.22.0 fix and leaks over HTTP](https://hackerone.com/reports/4071872)
   - Program: curl | Upvotes: 8 | Bounty: $0.00 | Type: Information Exposure Through Sent Data
192. [Use-after-free read of the freed referer buffer in `curl_easy_setopt(CURLOPT_REFERER)` — stale heap bytes transmitted in an outbound `Referer:` heade](https://hackerone.com/reports/4064040)
   - Program: curl | Upvotes: 29 | Bounty: $0.00 | Type: Information Disclosure
193. [HTML Injection in Contact Form Email Enables Phishing via Legitimate ████████ Infrastructure](https://hackerone.com/reports/3802451)
   - Program: Essity | Upvotes: 42 | Bounty: $0.00 | Type: Improper Output Neutralization for Logs
194. [Rustls backend discloses out-of-bounds heap data during legal IMAP upload cancellation](https://hackerone.com/reports/4085412)
   - Program: curl | Upvotes: 6 | Bounty: $0.00 | Type: Out-of-bounds Read
195. [IMAP literal size truncation on 32-bit platforms corrupts downloads and desynchronizes the response parser](https://hackerone.com/reports/4059104)
   - Program: curl | Upvotes: 9 | Bounty: $0.00 | Type: 
196. [Client-Side Denial of Service (DoS) via Memory Exhaustion on Password Reset Endpoint](https://hackerone.com/reports/3987499)
   - Program: Khan Academy | Upvotes: 32 | Bounty: $0.00 | Type: Uncontrolled Resource Consumption
197. [libmariadb ( mariadb-connector-c ): stack overflow via server-controlled field->length in prepared-statement codec](https://hackerone.com/reports/3766217)
   - Program: MariaDB | Upvotes: 23 | Bounty: $0.00 | Type: Stack Overflow
198. [Path Traversal in mbstream Extract](https://hackerone.com/reports/3678395)
   - Program: MariaDB | Upvotes: 29 | Bounty: $0.00 | Type: Path Traversal
199. [One-click cross-account JavaScript execution steals a victim write token through Turbo pagination and unattached Active Storage HTML](https://hackerone.com/reports/3943339)
   - Program: Basecamp | Upvotes: 49 | Bounty: $0.00 | Type: Cross-site Scripting (XSS) - Reflected
200. [IDOR allows user to access report details via reference.json endpoint](https://hackerone.com/reports/3862641)
   - Program: HackerOne | Upvotes: 372 | Bounty: $15000.00 | Type: Insecure Direct Object Reference (IDOR)
