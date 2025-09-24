# Changelog

## [0.12.0](https://github.com/scop/pytekukko-test/compare/v0.16.0...v0.12.0) (2025-09-24)


### Features

* error explicitly on unexpected response structures ([c7b493a](https://github.com/scop/pytekukko-test/commit/c7b493a37f4bcb6dda2d244691d6ee9feef06ec3))
* **examples:** add collection schedule printer ([75d7e0a](https://github.com/scop/pytekukko-test/commit/75d7e0a10f6b9589ca093d2e0354c1b541df59ee))
* **examples:** facilitate shtab generated completions ([0b89ac6](https://github.com/scop/pytekukko-test/commit/0b89ac6b9d5c33e003f1a5e1bfa131e74625f5a1))
* **examples:** icalendar option to --collection-schedules ([b9c51c6](https://github.com/scop/pytekukko-test/commit/b9c51c69b8a39489a673f9e1695899c1194ee6e8))
* **examples:** load env from $PYTEKUKKO_DOTENV, actually walk from cwd ([9ac3df4](https://github.com/scop/pytekukko-test/commit/9ac3df45d14ebd25b0037debb7070b08a6b4889a))
* **examples:** more -collection-schedules icalendar metadata ([1aee758](https://github.com/scop/pytekukko-test/commit/1aee758181a4dd1d5e469ef0c9a782d63547fdce))
* expose assumed service time zone ([2ed26e6](https://github.com/scop/pytekukko-test/commit/2ed26e6cf554278243438554fb8e3a994abd5c91))
* **models:** expose CustomerData.name ([c835fea](https://github.com/scop/pytekukko-test/commit/c835fea47a580c38f2eeb3d070369b98e57a7854))
* **python:** drop support for 3.9 ([6690293](https://github.com/scop/pytekukko-test/commit/669029352c047f726158388232d601f3ab564b47))
* remove Google calendar updater example ([c2f4c5c](https://github.com/scop/pytekukko-test/commit/c2f4c5c34824bcc3c91a2b7f82f57b971df98fe3))
* **retry:** improve login loop exception ([b0f66fb](https://github.com/scop/pytekukko-test/commit/b0f66fb98ff9d01a5607792cc756fe563e0796b9))


### Bug Fixes

* build vs publish testing ([0669b47](https://github.com/scop/pytekukko-test/commit/0669b474d4e95e343cc6696e700a87a326f403a4))
* build vs publish testing ([23f59e5](https://github.com/scop/pytekukko-test/commit/23f59e5a4c7e93f02597a73cf3f945361ae60a9a))
* **collection_schedule:** trigger login on HTTP bad request too ([8b196fd](https://github.com/scop/pytekukko-test/commit/8b196fd5a4b411ec1ac349fc04c39fefb68daea3))
* **dist:** actually include `py.typed` ([5822a46](https://github.com/scop/pytekukko-test/commit/5822a4614c1b9ad2a13c5727a66cc971e709ae76))
* **dist:** include `py.typed` ([afd09e7](https://github.com/scop/pytekukko-test/commit/afd09e7c95e4083846945a997bd9561aacf1c6f7))
* **dist:** include py.typed ([134eec2](https://github.com/scop/pytekukko-test/commit/134eec2b9990d06f24ab8af42f6372e55ecd9b73))
* **unmarshal:** times to timezone aware objects ([4523632](https://github.com/scop/pytekukko-test/commit/4523632ba0a7bd4b9f242b3b74d4255d90a428c9))


### Performance Improvements

* avoid some looped list appends ([85b03fb](https://github.com/scop/pytekukko-test/commit/85b03fb07ea9d8e420f3f6cd48513f6fc183affc))
* quote typing.cast type expressions ([76b5c56](https://github.com/scop/pytekukko-test/commit/76b5c566f49a2f385e89bbfaffaa3eb5dff1153e))


### Reverts

* don't error on pyparsing sre_constants 3.11 deprecation ([3b06256](https://github.com/scop/pytekukko-test/commit/3b06256602014fcbfbd343a5db6b644fdcc09a33))


### Documentation

* add OpenSSF Scorecard badge ([a2b1fa8](https://github.com/scop/pytekukko-test/commit/a2b1fa800e8493e999afbb13b0834848bfd75ce2))
* add OpenSSF Scorecard badge, misc tweaks ([5b70504](https://github.com/scop/pytekukko-test/commit/5b70504b5ffca34158cda3cbf96f36f0ed70d82c))
* **examples:** note .env loading in --help output ([b77e3f4](https://github.com/scop/pytekukko-test/commit/b77e3f4ce7a7a14e69191a40c7ed82d721a3c969))
* note Python in top level description ([adc916d](https://github.com/scop/pytekukko-test/commit/adc916d65a7a781071baa047e9478e87860acbff))
* **readme:** elaborate disclaimer a bit ([f0e87b1](https://github.com/scop/pytekukko-test/commit/f0e87b16737d1cbbcf25dc7e527223ed87921261))
* **readme:** run through prettier ([157ed3b](https://github.com/scop/pytekukko-test/commit/157ed3b51bc874936e9588a17ee6ad20153595eb))
* **ruff:** update ignored rule commentary ([778a00b](https://github.com/scop/pytekukko-test/commit/778a00b3f904cac7e169e94c70acee4906fdf62b))
* spelling and grammar fixes ([4bf6eb9](https://github.com/scop/pytekukko-test/commit/4bf6eb9207d9f0ddfdf12a482ea4066882a64537))


### Miscellaneous Chores

* **python:** drop support for 3.8 ([6ca7a09](https://github.com/scop/pytekukko-test/commit/6ca7a098b0f04e36a6ba421c9bd9309d03fc4616))

## [0.16.0](https://github.com/scop/pytekukko/compare/v0.15.0...v0.16.0) (2024-01-23)


### Features

* **examples:** more -collection-schedules icalendar metadata ([1aee758](https://github.com/scop/pytekukko/commit/1aee758181a4dd1d5e469ef0c9a782d63547fdce))

## [0.15.0](https://github.com/scop/pytekukko/compare/v0.14.0...v0.15.0) (2024-01-22)


### Features

* **examples:** icalendar option to --collection-schedules ([b9c51c6](https://github.com/scop/pytekukko/commit/b9c51c69b8a39489a673f9e1695899c1194ee6e8))

## [0.14.0](https://github.com/scop/pytekukko/compare/v0.13.0...v0.14.0) (2023-07-25)


### Features

* **python:** drop support for 3.9 ([6690293](https://github.com/scop/pytekukko/commit/669029352c047f726158388232d601f3ab564b47))


### Performance Improvements

* avoid some looped list appends ([85b03fb](https://github.com/scop/pytekukko/commit/85b03fb07ea9d8e420f3f6cd48513f6fc183affc))

## [0.13.0](https://github.com/scop/pytekukko/compare/v0.12.1...v0.13.0) (2023-02-03)


### Features

* error explicitly on unexpected response structures ([c7b493a](https://github.com/scop/pytekukko/commit/c7b493a37f4bcb6dda2d244691d6ee9feef06ec3))
* expose assumed service time zone ([2ed26e6](https://github.com/scop/pytekukko/commit/2ed26e6cf554278243438554fb8e3a994abd5c91))


### Bug Fixes

* **unmarshal:** times to timezone aware objects ([4523632](https://github.com/scop/pytekukko/commit/4523632ba0a7bd4b9f242b3b74d4255d90a428c9))

## [0.12.1](https://github.com/scop/pytekukko/compare/v0.12.0...v0.12.1) (2022-11-12)


### Bug Fixes

* **dist:** actually include `py.typed` ([5822a46](https://github.com/scop/pytekukko/commit/5822a4614c1b9ad2a13c5727a66cc971e709ae76))

## [0.12.0](https://github.com/scop/pytekukko/compare/v0.11.0...v0.12.0) (2022-11-12)


### Bug Fixes

* **dist:** include py.typed ([134eec2](https://github.com/scop/pytekukko/commit/134eec2b9990d06f24ab8af42f6372e55ecd9b73))


### Reverts

* don't error on pyparsing sre_constants 3.11 deprecation ([3b06256](https://github.com/scop/pytekukko/commit/3b06256602014fcbfbd343a5db6b644fdcc09a33))


### Miscellaneous Chores

* **python:** drop support for 3.8 ([6ca7a09](https://github.com/scop/pytekukko/commit/6ca7a098b0f04e36a6ba421c9bd9309d03fc4616))

## [0.11.0](https://github.com/scop/pytekukko/compare/v0.10.0...v0.11.0) (2022-03-26)


### Features

* **models:** expose CustomerData.name ([c835fea](https://github.com/scop/pytekukko/commit/c835fea47a580c38f2eeb3d070369b98e57a7854))

## [0.10.0](https://www.github.com/scop/pytekukko/compare/v0.9.0...v0.10.0) (2021-12-06)


### Features

* **examples:** load env from $PYTEKUKKO_DOTENV, actually walk from cwd ([9ac3df4](https://www.github.com/scop/pytekukko/commit/9ac3df45d14ebd25b0037debb7070b08a6b4889a))


### Documentation

* **readme:** elaborate disclaimer a bit ([f0e87b1](https://www.github.com/scop/pytekukko/commit/f0e87b16737d1cbbcf25dc7e527223ed87921261))

## 0.9.0 (2021-12-06)


### Features

* **examples:** add collection schedule printer ([75d7e0a](https://www.github.com/scop/pytekukko/commit/75d7e0a10f6b9589ca093d2e0354c1b541df59ee))
* **examples:** add invoice header example ([fe62a74](https://www.github.com/scop/pytekukko/commit/fe62a748d3ac219460f1e146762fca6b169cc0c2))
* **examples:** output JSON from print_next_collection_dates ([8d7f7e8](https://www.github.com/scop/pytekukko/commit/8d7f7e83325db0bf74302bcb0d0c2ab45363e3a4))
* first somewhat complete version ([b5fa4d9](https://www.github.com/scop/pytekukko/commit/b5fa4d9105044f9159e9b6b517a3dc52575cd523))
* **models:** add InvoiceHeader name, due_date and total ([24ab20e](https://www.github.com/scop/pytekukko/commit/24ab20e87ed5f81ee18b414f52319ce9631f3113))
* **retry:** improve login loop exception ([b0f66fb](https://www.github.com/scop/pytekukko/commit/b0f66fb98ff9d01a5607792cc756fe563e0796b9))


### Bug Fixes

* **collection_schedule:** trigger login on HTTP bad request too ([8b196fd](https://www.github.com/scop/pytekukko/commit/8b196fd5a4b411ec1ac349fc04c39fefb68daea3))
* **get_collection_schedule:** auto re-login on internal server error ([2540feb](https://www.github.com/scop/pytekukko/commit/2540feb2b535d0595f317e82bf1a0a599b936da6))
* **models:** remove InvoiceHeader.customer_number ([f52345e](https://www.github.com/scop/pytekukko/commit/f52345e191d0ff95b150e844936fc9b474fbd45d))


### Miscellaneous Chores

* release next as 0.9.0 ([36ab8eb](https://www.github.com/scop/pytekukko/commit/36ab8ebfc9325f25146c1402ed555a6f7c811a78))


### Documentation

* **examples:** add required Google Calendar data notes ([b3df6dc](https://www.github.com/scop/pytekukko/commit/b3df6dcec13ce4448680003ffdb24f2f3bf756e4))
* **examples:** note .env loading in --help output ([b77e3f4](https://www.github.com/scop/pytekukko/commit/b77e3f4ce7a7a14e69191a40c7ed82d721a3c969))
* improve and be consistent with project description ([1f64578](https://www.github.com/scop/pytekukko/commit/1f6457834755989e3eac855e5739778d4bfe2145))
* **readme:** add disclaimer ([2aaf32c](https://www.github.com/scop/pytekukko/commit/2aaf32c33d3fcb855524183760314e9ed2662222))
* **readme:** clarify what API uses cookies ([7c5e1d2](https://www.github.com/scop/pytekukko/commit/7c5e1d27905cb3f31357cdad99408d8b3636dc2f))
* **readme:** elaborate on design and goals a bit ([6791b76](https://www.github.com/scop/pytekukko/commit/6791b76cfaee3a499b9021337f98edb257715ae5))
* **readme:** initial write up ([fb7588a](https://www.github.com/scop/pytekukko/commit/fb7588aa0a52f7c8c5464bcbeece7ae1a46adfc3))
* **readme:** link to aiohttp objects ([4eea46a](https://www.github.com/scop/pytekukko/commit/4eea46ac44e1afa7257f3ad38de4c4d6caf32844))
* **readme:** run through prettier ([157ed3b](https://www.github.com/scop/pytekukko/commit/157ed3b51bc874936e9588a17ee6ad20153595eb))
* **readme:** wording tweaks ([2d01861](https://www.github.com/scop/pytekukko/commit/2d01861a01faabef758ec102e19b5670f2665b42))
* **requirements-test:** comment grammar fix ([2b91980](https://www.github.com/scop/pytekukko/commit/2b91980bd9c1642b1fcbab0cca778ebc10dc8375))
* spelling and grammar fixes ([4bf6eb9](https://www.github.com/scop/pytekukko/commit/4bf6eb9207d9f0ddfdf12a482ea4066882a64537))
* **version:** docstring copy-pasto fix ([4f0207e](https://www.github.com/scop/pytekukko/commit/4f0207ec417b47e5ba55898653bd3e1085e036d8))
