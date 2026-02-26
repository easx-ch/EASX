To ensure secure identification of individuals within the pension fund system, 
a unique identifier known as `Personal Hash` is generated and used in the EASX Server APIs
for each insured individual. This method enhances privacy and security by ensuring
that personal information is not directly exposed within the system.

NOTE: For convenience, when using the EAS Client API, the PersonalHash is calculated automatically,
and there is no need for manual generation during API calls.

# Format and Algorithm
- **Pattern:** The input for the hashing algorithm must follow the pattern `[SVNumber]_[Birthdate]`. 
  Here, `[SVNumber]` is the social ecurity number fromatted with dots (i.e., '756.9999.9999.91'),
  and [Birthdate] is formatted according to the ISO 8601 date format 'YYYY-MM-DD' (i.e., '1980-02-28'),
  without time and zone components.
- **Algorithm:** The [SHA-256](https://en.wikipedia.org/wiki/SHA-2) hashing algorithm is used to 
  generate the hash. This algorithm is chosen for its strong cryptographic security, ensuring that
  the hash cannot be reversed to reveal personal information.

# Example
Consider an individual with the social security number `756.9999.9999.91` and a birthdate of `28th February 1980`.
The input string for the SHA-256 algorithm would be `756.9999.9999.91_1980-02-28`. Processing this input
generates a `personalHash` as follows:

- **Input:** `756.9999.9999.91_1980-02-28`
- **Generated `personalHash`:** `5fe1aa4d283137ba492726d4865c12f2bdff32ee7340b3b3e2b11f5f81ffcf0d`
