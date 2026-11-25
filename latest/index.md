# synapser

**Important Note About the R Client**

We maintain the R client to support our R user community, recognizing R
as a foundational language in many data workflows. synapser is built on
top of the [Synapse Python client](https://python-docs.synapse.org/) via
the reticulate package. This lets us solve complex engineering problems,
such as file transfers and caching, once in Python and reuse those
solutions in R.

We recommend upgrading to version 3.0 or later of the Synapse R client.
Starting with 3.0, the R client uses reticulate to manage its Python
dependencies, which should make installation and updates easier. You do
not need to set up Python yourself: reticulate installs a compatible
Python and the Synapse Python client the first time synapser is loaded.

If you run into problems, see the [Troubleshooting
guide](https://linglp.github.io/synapser/latest/articles/troubleshooting.md)
or [open an issue](https://github.com/Sage-Bionetworks/synapser/issues).
New features usually appear in the Python client first, so if you need
one that synapser does not have yet, you can use the Python client
directly. If you continue to run into environment or package version
issues, you can also use the Synapse Python client via reticulate. See
the [Using synapseclient with R through
reticulate](https://python-docs.synapse.org/en/stable/tutorials/reticulate/).

We appreciate your patience and continued feedback as we work to improve
the user experience across both clients.

**Introducing synapser 3.0.0**

synapser 3.0.0 is a major release built on version 4.15 of the Synapse
Python client. It introduces object-oriented models: create an instance
of a Synapse object, such as
`File(path = “data.csv”, parent_id = “syn123”)`, then pipe it into verb
functions like
[`synStore()`](https://linglp.github.io/synapser/latest/reference/synStore.md)
and
[`synGet()`](https://linglp.github.io/synapser/latest/reference/synGet.md).
It also brings:

- **No Python setup.** When synapser is loaded, reticulate installs a
  compatible Python and the Synapse Python client for you. Python
  versions 3.11 to 3.15 are supported.
- **Current R dependencies.** synapser works with current versions of
  reticulate (1.44.0 or later) and rjson, and requires R 4.2.0 or later.

**This release is not backward compatible.** Functions from earlier
versions, such as `synGetChildren()` and `synGetAnnotations()`, have
been removed. Before upgrading, see [Key differences from the legacy
API](https://linglp.github.io/synapser/latest/articles/data_upload_download.html#key-differences-from-the-legacy-api)
for how earlier calls map to the new API, and [Supported Models and
Functions](#supported-models-and-functions) for what this release
supports.

## Introduction

The `synapser` package provides an interface to
[Synapse](https://www.synapse.org), a collaborative workspace for
reproducible data-intensive research projects, providing support for:

- integrated presentation of data, code, and text
- fine-grained access control
- provenance tracking

The `synapser` package lets you communicate with the Synapse platform to
create collaborative data analysis projects and access data using the R
programming language. Other Synapse clients exist for
[Python](https://python-docs.synapse.org/),
[Java](https://github.com/Sage-Bionetworks/Synapse-Repository-Services/tree/develop/client/synapseJavaClient),
and [the web browser](https://www.synapse.org).

## Supported Models and Functions

synapser 3.0.0 supports the following Synapse models. Each model’s
reference page also lists the functions that work on it, such as
`synGetAcl()`, `synSetPermissions()`, or `synSyncFromSynapse()`.

| Area | Models |
|----|----|
| Projects, folders, and files | [`Project`](https://linglp.github.io/synapser/latest/reference/Project.md), [`Folder`](https://linglp.github.io/synapser/latest/reference/Folder.md), [`File`](https://linglp.github.io/synapser/latest/reference/File.md), [`Link`](https://linglp.github.io/synapser/latest/reference/Link.md) |
| Tables and views | [`Table`](https://linglp.github.io/synapser/latest/reference/Table.md), [`Column`](https://linglp.github.io/synapser/latest/reference/Column.md), [`JsonSubColumn`](https://linglp.github.io/synapser/latest/reference/JsonSubColumn.md), [`VirtualTable`](https://linglp.github.io/synapser/latest/reference/VirtualTable.md), [`EntityView`](https://linglp.github.io/synapser/latest/reference/EntityView.md), [`MaterializedView`](https://linglp.github.io/synapser/latest/reference/MaterializedView.md), [`SubmissionView`](https://linglp.github.io/synapser/latest/reference/SubmissionView.md), [`Dataset`](https://linglp.github.io/synapser/latest/reference/Dataset.md), [`DatasetCollection`](https://linglp.github.io/synapser/latest/reference/DatasetCollection.md), [`EntityRef`](https://linglp.github.io/synapser/latest/reference/EntityRef.md) |
| Provenance | [`Activity`](https://linglp.github.io/synapser/latest/reference/Activity.md), [`UsedEntity`](https://linglp.github.io/synapser/latest/reference/UsedEntity.md), [`UsedURL`](https://linglp.github.io/synapser/latest/reference/UsedURL.md) |
| Wikis | [`WikiPage`](https://linglp.github.io/synapser/latest/reference/WikiPage.md), [`WikiHeader`](https://linglp.github.io/synapser/latest/reference/WikiHeader.md), [`WikiHistorySnapshot`](https://linglp.github.io/synapser/latest/reference/WikiHistorySnapshot.md), [`WikiOrderHint`](https://linglp.github.io/synapser/latest/reference/WikiOrderHint.md) |
| Challenges and evaluations | [`Evaluation`](https://linglp.github.io/synapser/latest/reference/Evaluation.md), [`Submission`](https://linglp.github.io/synapser/latest/reference/Submission.md), [`SubmissionStatus`](https://linglp.github.io/synapser/latest/reference/SubmissionStatus.md), [`SubmissionBundle`](https://linglp.github.io/synapser/latest/reference/SubmissionBundle.md) |
| Users, teams, and organizations | [`Team`](https://linglp.github.io/synapser/latest/reference/Team.md), [`UserProfile`](https://linglp.github.io/synapser/latest/reference/UserProfile.md), [`UserPreference`](https://linglp.github.io/synapser/latest/reference/UserPreference.md), [`Organization`](https://linglp.github.io/synapser/latest/reference/Organization.md), [`JSONSchema`](https://linglp.github.io/synapser/latest/reference/JSONSchema.md) |
| Storage | [`StorageLocation`](https://linglp.github.io/synapser/latest/reference/StorageLocation.md), [`StorageLocationType`](https://linglp.github.io/synapser/latest/reference/StorageLocationType.md) |
| AI agents | [`Agent`](https://linglp.github.io/synapser/latest/reference/Agent.md), [`AgentSession`](https://linglp.github.io/synapser/latest/reference/AgentSession.md), [`AgentPrompt`](https://linglp.github.io/synapser/latest/reference/AgentPrompt.md) |

These functions work across models:

| Task | Functions |
|----|----|
| Connecting to Synapse | [`synLogin`](https://linglp.github.io/synapser/latest/reference/synLogin.md), [`synLogout`](https://linglp.github.io/synapser/latest/reference/synLogout.md), [`synSetEndpoints`](https://linglp.github.io/synapser/latest/reference/synSetEndpoints.md) |
| Getting, storing, and deleting entities | [`synGet`](https://linglp.github.io/synapser/latest/reference/synGet.md), [`synStore`](https://linglp.github.io/synapser/latest/reference/synStore.md), [`synDelete`](https://linglp.github.io/synapser/latest/reference/synDelete.md), [`synSetProperties`](https://linglp.github.io/synapser/latest/reference/synSetProperties.md) |
| Options for getting and storing | [`FileOptions`](https://linglp.github.io/synapser/latest/reference/FileOptions.md), [`ActivityOptions`](https://linglp.github.io/synapser/latest/reference/ActivityOptions.md), [`TableOptions`](https://linglp.github.io/synapser/latest/reference/TableOptions.md), [`LinkOptions`](https://linglp.github.io/synapser/latest/reference/LinkOptions.md), [`StoreFileOptions`](https://linglp.github.io/synapser/latest/reference/StoreFileOptions.md), [`StoreContainerOptions`](https://linglp.github.io/synapser/latest/reference/StoreContainerOptions.md), [`StoreTableOptions`](https://linglp.github.io/synapser/latest/reference/StoreTableOptions.md), [`StoreJSONSchemaOptions`](https://linglp.github.io/synapser/latest/reference/StoreJSONSchemaOptions.md), [`StoreGridOptions`](https://linglp.github.io/synapser/latest/reference/StoreGridOptions.md) |
| Querying tables and views | [`synQuery`](https://linglp.github.io/synapser/latest/reference/Table_Query.md), [`synQueryPartMask`](https://linglp.github.io/synapser/latest/reference/Table_QueryPartMask.md) |
| Download list (cart) | [`synDownloadListAdd`](https://linglp.github.io/synapser/latest/reference/synDownloadListAdd.md), [`synDownloadListRemove`](https://linglp.github.io/synapser/latest/reference/synDownloadListRemove.md), [`synDownloadListClear`](https://linglp.github.io/synapser/latest/reference/synDownloadListClear.md), [`synDownloadListManifest`](https://linglp.github.io/synapser/latest/reference/synDownloadListManifest.md), [`synDownloadListFiles`](https://linglp.github.io/synapser/latest/reference/synDownloadListFiles.md), [`DownloadListItem`](https://linglp.github.io/synapser/latest/reference/DownloadListItem.md) |
| Utilities | [`synFindEntityId`](https://linglp.github.io/synapser/latest/reference/synFindEntityId.md), [`synIsSynapseId`](https://linglp.github.io/synapser/latest/reference/synIsSynapseId.md), [`synOnweb`](https://linglp.github.io/synapser/latest/reference/synOnweb.md), [`synPrintEntity`](https://linglp.github.io/synapser/latest/reference/synPrintEntity.md), [`synMd5Query`](https://linglp.github.io/synapser/latest/reference/synMd5Query.md), [`synSendMessage`](https://linglp.github.io/synapser/latest/reference/synSendMessage.md) |
| REST API | [`synRestGet`](https://linglp.github.io/synapser/latest/reference/synRestGet.md), [`synRestPost`](https://linglp.github.io/synapser/latest/reference/synRestPost.md), [`synRestPut`](https://linglp.github.io/synapser/latest/reference/synRestPut.md), [`synRestDelete`](https://linglp.github.io/synapser/latest/reference/synRestDelete.md) |

See the [reference
index](https://linglp.github.io/synapser/latest/reference/index.md) for
the full list.

## Requirements

- R version 4.2.0 or higher (tested up to R 4.6.1)
- reticulate 1.44.0 or higher
- [Synapse account](https://www.synapse.org/register)

**Note:** You do not need to install Python yourself. When `synapser` is
loaded, it declares its Python requirement via
[`reticulate::py_require()`](https://rstudio.github.io/reticulate/reference/py_require.html),
and reticulate downloads a compatible Python and the Synapse Python
client into a managed environment on first use.

## Documentation

Full documentation for `synapser` is on the [docs
site](https://r-docs.synapse.org/):

- [Reference](https://r-docs.synapse.org/reference/index.html): every
  model and function, organized by model.
- [Installation](https://r-docs.synapse.org/articles/installation.html),
  [Authentication](https://r-docs.synapse.org/articles/authentication.html),
  and
  [Configuration](https://r-docs.synapse.org/articles/configuration.html):
  get set up.
- [Tutorials](https://r-docs.synapse.org/articles/index.html): task
  guides for files, folders, tables, wikis, evaluations, and more.
- [Migrating to synapser
  3.0](https://r-docs.synapse.org/articles/migration_to_synapser_3_0.html):
  how to update scripts written for synapser 2.x.

## Installation

`synapser` 3.0.0 is distributed through
[R-universe](https://sage-bionetworks.r-universe.dev/synapser), which
provides ready-built binaries for Windows and macOS (Apple silicon and
Intel). Install it with:

\
[`install.packages`](https://rdrr.io/r/utils/install.packages.html)`(`\
`  ``"synapser"``,`\
`  repos ``=`` `[`c`](https://rdrr.io/r/base/c.html)`(``"https://sage-bionetworks.r-universe.dev"``, ``"https://cloud.r-project.org"``)`\
`)`

Listing CRAN alongside R-universe lets R pull synapser’s dependencies
(such as `reticulate` and `rjson`) from CRAN.

**Linux:** R installs packages from source on Linux, and several of
synapser’s dependencies contain compiled code. Install a C/C++ compiler
and the libpng headers first, then run the command above:

``` bash
# Ubuntu / Debian
sudo apt-get install -y build-essential libpng-dev
# Amazon Linux / RHEL / CentOS
sudo dnf install -y gcc gcc-c++ make libpng-devel
```

Then restart R and verify the installation:

\
[`library`](https://rdrr.io/r/base/library.html)`(`[`synapser`](https://github.com/Sage-Bionetworks/synapser)`)`\
[`packageVersion`](https://rdrr.io/r/utils/packageDescription.html)`(``"synapser"``)``  ``# should be 3.0.0`

The first
[`library(synapser)`](https://github.com/Sage-Bionetworks/synapser) may
take a minute while reticulate downloads Python and the Synapse Python
client. Later loads reuse the cached environment.

[**See the install
guide**](https://linglp.github.io/synapser/latest/articles/installation.md)
for upgrading from synapser 2.x, installing an older version (2.x
releases remain on [RAN](http://ran.synapse.org)), installing from
GitHub, and how synapser finds Python. If installation fails, see the
[Troubleshooting
guide](https://linglp.github.io/synapser/latest/articles/troubleshooting.md).

## Usage

To get started, try logging in to Synapse. If you don’t already have a
Synapse account, register [here](https://www.synapse.org/register):

\
[`library`](https://rdrr.io/r/base/library.html)`(`[`synapser`](https://github.com/Sage-Bionetworks/synapser)`)`\
[`synLogin`](https://linglp.github.io/synapser/latest/reference/synLogin.md)`(``)`

To learn more about using `synapser`, visit the [docs
site](https://r-docs.synapse.org/) or browse the package vignettes:

\
[`browseVignettes`](https://rdrr.io/r/utils/browseVignettes.html)`(``package ``=`` ``"synapser"``)`
