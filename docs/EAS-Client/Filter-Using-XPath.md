The EASClient provides an extension to the EASX Hub API to retrieve a filtered list of FZL documents using an XPath expression. This is very useful when not processing incoming documents immediately on first retrieval, but only when
it is needed, for example when a payment has arrived.

# Introduction
An optional 'xPathFilter' parameter on getting incoming documents (GET /api/eas/v1/documents) can be set with a valid XPath 2.0 expression to filter the incoming documents.

# Configuration
Note that the DocumentCacheMode configuration must be set to either 'EnabledWithoutPrefetch' or 'Enabled' to utilize this feature. It enables documents to be fetched and cached locally and will allow performant repeated filtering.

# XPath syntax

The given expression must conform to the [XPath 2.0 specification](https://www.w3.org/TR/xpath20/). Any incoming FZL documents will be returned for which the XPath expression returns either an XML node, a non-empty list of XML nodes or a text, true or non-zero value.

[XPath Functions](https://www.w3.org/2006/xpath-functions/) (like lower-case(), matches(), etc.) can be used.

To access nodes for the payment schema (http<nolink>://www.chaeis.ch/xsd/Zahlungsverkehr-1.1) use 'zah:' as namespace prefix. The default namespace will be the FZL schema (t.i. http<nolink>://exchange.aeis.ch/xsd/FZL-1.X).

# Examples

Following are some sample XPath expressions that could be used. To try them out you can use [the sample document](https://easxcommonstorage.blob.core.windows.net/demo-assets/echo-demo-fzl-1-5.xml) from the [getting started](../Getting-Started.md) section.

- Retrieve all documents with a payment amount of '1000.10'<br/>
```/UEBERTRAGUNG//FZL/zah:ZAHLUNG/zah:BETRAG = 1000.10```

- Retrieve all documents with social number '001.11.000.000' and an payment amount between 999.10 and 1001.10<br/>
```//FZL[PERSON_AHV/AHV_NUMMER = '001.11.000.000' and zah:ZAHLUNG/zah:BETRAG > 999.10 and zah:ZAHLUNG/zah:BETRAG < 1001.10]```

- Retrieve all documents with persons name equals 'mustermann' and first name 'max' case-insensitive<br/>
```//FZL/PERSON_AHV[lower-case(NACHNAME) = "mustermann" and lower-case(VORNAME) = "max"]```

- Retrieve all documents with persons name equals 'mustermann' and first name starts with 'max' case-insensitive<br/>
```//FZL[lower-case(PERSON_AHV/NACHNAME) = "mustermann" and matches(PERSON_AHV/VORNAME, '^max', 'i')]```

