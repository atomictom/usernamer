# Usernamer

This is a simple utility to try to generate random pronounceable usernames. This
can be used by the security-minded (or paranoid) to make it more difficult for an
attacker to find your accounts.

## Example

```
$ ./usernamer.py
milamu
choddousda
nebafi
bipceshta
nimvichi
jisachbe
shaprioummi
negkuri
chaophmasso
befoitto
```

## Why use a random username?

It makes it [harder for attackers to tie your accounts together or carry out
targeted attacks][username-attacks]. Tying your accounts together can possibly
lead to a larger breach of privacy (especially if you re-use passwords, which
[you shouldn't][password reuse]) as attackers can get more info on you. Knowing
your username also makes it easier to carry out targeted attacks like [account
recovery attacks][account recovery attacks][1].

Additionally, [some providers treat usernames as a secret][username-secret].

[1]: That is, where a hacker goes through the account recovery process to
  bypass needing a password.

[username-attacks]: https://www.tomsguide.com/us/single-username-risks,news-18288.html
[username-secret]: https://krebsonsecurity.com/2018/03/what-is-your-banks-security-banking-on/
[password reuse]: https://www.tomsguide.com/reference/why-never-reuse-password
[account recovery attacks]: https://www.wired.com/2012/08/apple-amazon-mat-honan-hacking/

## Why to not use a random username

If you're not doing any of the following, you should probably do these first:

* Use a password manager. Without this, remembering your random usernames might
  be quite difficult!
* Don't re-use passwords. A random username shouldn't be the way you address
  password re-use. Instead, use a password manager and generate random passwords
  for each service.
* Use [MFA][MFA]. Preferrably [FIDO(2)/WebAuthn][fido] security keys (e.g.
  [Yubikeys][Yubikeys]). OTP also works well (e.g. [Authy][Authy], [Google
  Authenticator][Google Authenticator])[2].  Lastly, using text-based MFA is
  (probably) better than nothing[3].

Random usernames should not be a cornerstone of your security policy, but rather
a mitigation to specific attacks (making it easy for attackers to tie your
accounts together or do targeted attacks on your accounts).

[2]: FIDO(2) protects against [man-in-the-middle][mitm] attacks which OTP does
  not. While a MitM attack on OTP won't get the secret, it can be used to login
  immediately.

[3]: But it's susceptible to [sim-jacking attacks][sim-jacking].

[MFA]: https://en.wikipedia.org/wiki/Multi-factor_authentication
[fido]: https://doubleoctopus.com/blog/your-complete-guide-to-fido-fast-identity-online/
[Yubikeys]: https://www.yubico.com/products/
[Authy]: https://authy.com/
[Google Authenticator]: https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en_IE
[mitm]: https://en.wikipedia.org/wiki/Man-in-the-middle_attack
[sim-jacking]: https://www.wired.com/story/sim-swap-attack-defend-phone/

## Why should I use this?

No particular reason. The code is quite short so it's easy to manually verify
it's not doing anything weird. Other username generators might be better,
though.
