The EAS Client provides an extension to the EASX Hub API to retrieve FZL documents and attachments as PDFs.
This functionality enables data to be presented in a user-readable format, especially when data is unstructured 
or your system does not yet support importing elements from newer FZL versions.

# Getting the PDF of a document

To retrieve the PDF of an FZL document, use the following endpoint:
```GET /api/eas/v1/in-documents/{id}```

In this request, pass the parameter `format` with the value `'pdf'`.

## Language Selection

The PDF can be generated in multiple languages. Use the `language` parameter to specify the language, selecting from the following supported values:
- `'de'` for German
- `'fr'` for French
- `'en'` for English

## Filtering Options

Additional parameters can be used to customize the PDF content:

- **noAttachments**: If set to `true`, attachments will be excluded from the PDF.
- **ahvOrSozv**: Filters the PDF content to include only FZL data for the individual with the specified Social or AHV Number.
- **fzlPositions**: Limits the PDF content to specific positions in the FZL document. This parameter accepts a list of position indexes, starting from 0.