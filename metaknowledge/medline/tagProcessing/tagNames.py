from ...WOS.tagProcessing.helpFuncs import makeBiDirectional


authorBasedTags = [
    'AD',
    'AUID',
]

tagNameDict = {
"Abstract" : "AB",
"CopyrightInformation" : "CI",
"Affiliation" : "AD",
"InvestigatorAffiliation" : "IRAD",
"ArticleIdentifier" : "AID",
"Author" : "AU",
"AuthorIdentifier" : "AUID",
"FullAuthor" : "FAU",
"BookTitle" : "BTI",
"CollectionTitle" : "CTI",
"CorporateAuthor" : "CN",
"CreateDate" : "CRDT",
"DateCompleted" : "DCOM",
"DateCreated" : "DA",
"DateLastRevised" : "LR",
"DateElectronicPublication" : "DEP",
"DatePublication" : "DP",
"Edition" : "EN",
"Editor" : "ED",
"Editor" : "FED",
"EntrezDate" : "EDAT",
"GeneSymbol" : "GS",
"GeneralNote" : "GN",
"GrantNumber" : "GR",
"Investigator" : "IR",
"InvestigatorFull" : "FIR",
"ISBN" : "ISBN",
"ISSN" : "IS",
"Issue" : "IP",
"JournalTitleAbbreviation" : "TA",
"JournalTitle" : "JT",
"Language" : "LA",
"LocationIdentifier" : "LID",
"ManuscriptIdentifier" : "MID",
"MeSHDate" : "MHDA",
"MeSHTerms" : "MH",
"NLMID" : "JID",
"NumberReferences" : "RF",
"OtherAbstract" : "OAB",
"OtherAbstract" : "OABL",
"OtherCopyright" : "OCI",
"OtherID" : "OID",
"OtherTerm" : "OT",
"OtherTermOwner" : "OTO",
"Owner" : "OWN",
"Pagination" : "PG",
"PersonalNameSubject" : "PS",
"FullPersonalNameSubject" : "FPS",
"PlacePublication" : "PL",
"PublicationHistoryStatus" : "PHST",
"PublicationStatus" : "PST",
"PublicationType" : "PT",
"PublishingModel" : "PUBM",
"PubMedCentralIdentifier" : "PMC",
"PubMedCentralRelease" : "PMCR",
"PubMedUniqueIdentifier" : "PMID",
"RegistryNumber" : "RN",
"SubstanceName" : "NM",
"SecondarySourceID" : "SI",
"Source" : "SO",
"SpaceFlightMission" : "SFM",
"Status" : "STAT",
"Subset" : "SB",
"Title" : "TI",
"TransliteratedTitle" : "TT",
"Volume" : "VI",
"VolumeTitle" : "VTI",
"CommentIn" : "CIN",
"ErratumIn" : "EIN",
"ErratumFor" : "EFR",
"CorrectedRepublishedIn" : "CRI",
"CorrectedRepublishedFrom" : "CRF",
"DatasetIn" : "DDIN",
"DatasetUseReportedIn" : "DRIN",
"PartialRetractionIn" : "PRIN",
"PartialRetractionOf" : "PROF",
"RepublishedIn" : "RPI",
"RepublishedFrom" : "RPF",
"RetractionIn" : "RIN",
"RetractionOf" : "ROF",
"UpdateIn" : "UIN",
"UpdateOf" : "UOF",
"SummaryForPatients" : "SPIN",
"OriginalReportIn" : "ORI",
}

tagNameConverterDict = makeBiDirectional(tagNameDict)
