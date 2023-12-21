# Changelog

## [0.6.5](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.6.4...google-cloud-gke-multicloud-v0.6.5) (2023-12-21)


### Features

* added Binary Authorization support which is a deploy-time security control that ensures only trusted container images are deployed ([30f5d0e](https://github.com/googleapis/google-cloud-python/commit/30f5d0ef8ee52c3a30f1cdd166f69d76c0a3366a))
* added force-deletion support for AWS Clusters & Node Pools ([30f5d0e](https://github.com/googleapis/google-cloud-python/commit/30f5d0ef8ee52c3a30f1cdd166f69d76c0a3366a))
* added proxy support for Attached Clusters ([30f5d0e](https://github.com/googleapis/google-cloud-python/commit/30f5d0ef8ee52c3a30f1cdd166f69d76c0a3366a))
* added support for a new admin-groups flag in the create and update APIs ([30f5d0e](https://github.com/googleapis/google-cloud-python/commit/30f5d0ef8ee52c3a30f1cdd166f69d76c0a3366a))
* added support for EC2 Spot instance types for AWS Node Pools ([30f5d0e](https://github.com/googleapis/google-cloud-python/commit/30f5d0ef8ee52c3a30f1cdd166f69d76c0a3366a))
* added support for per-node-pool subnet security group rules for AWS Node Pools ([30f5d0e](https://github.com/googleapis/google-cloud-python/commit/30f5d0ef8ee52c3a30f1cdd166f69d76c0a3366a))
* added Surge Update and Rollback support for AWS Node Pools ([30f5d0e](https://github.com/googleapis/google-cloud-python/commit/30f5d0ef8ee52c3a30f1cdd166f69d76c0a3366a))
* expanded Kubernetes version info ([30f5d0e](https://github.com/googleapis/google-cloud-python/commit/30f5d0ef8ee52c3a30f1cdd166f69d76c0a3366a))


### Documentation

* updated comments of existing fields ([30f5d0e](https://github.com/googleapis/google-cloud-python/commit/30f5d0ef8ee52c3a30f1cdd166f69d76c0a3366a))

## [0.6.4](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.6.3...google-cloud-gke-multicloud-v0.6.4) (2023-12-07)


### Features

* Add support for python 3.12 ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))
* Introduce compatibility with native namespace packages ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))


### Bug Fixes

* Require proto-plus &gt;= 1.22.3 ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))
* Use `retry_async` instead of `retry` in async client ([fb6f9db](https://github.com/googleapis/google-cloud-python/commit/fb6f9dbfadfe1a8ca3b236e0cae5c85cf2862f3e))

## [0.6.3](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.6.2...google-cloud-gke-multicloud-v0.6.3) (2023-09-19)


### Documentation

* Minor formatting ([#11632](https://github.com/googleapis/google-cloud-python/issues/11632)) ([dbee08f](https://github.com/googleapis/google-cloud-python/commit/dbee08f2df63e1906ba13b0d3060eec5a80c79e2))

## [0.6.2](https://github.com/googleapis/google-cloud-python/compare/google-cloud-gke-multicloud-v0.6.1...google-cloud-gke-multicloud-v0.6.2) (2023-07-05)


### Bug Fixes

* Add async context manager return types ([#11446](https://github.com/googleapis/google-cloud-python/issues/11446)) ([37682b7](https://github.com/googleapis/google-cloud-python/commit/37682b7793cfe0dcb27963fea7e474b3b85571c9))

## [0.6.1](https://github.com/googleapis/python-gke-multicloud/compare/v0.6.0...v0.6.1) (2023-03-23)


### Documentation

* Fix formatting of request arg in docstring ([#66](https://github.com/googleapis/python-gke-multicloud/issues/66)) ([cabb6f7](https://github.com/googleapis/python-gke-multicloud/commit/cabb6f70c159dd06f34b03bff36f005d0cc08d35))

## [0.6.0](https://github.com/googleapis/python-gke-multicloud/compare/v0.5.1...v0.6.0) (2023-02-02)


### Features

* Added `reconciling` and `update_time` output fields to Azure Client resource. ([76ed673](https://github.com/googleapis/python-gke-multicloud/commit/76ed673d5438471fa90cf2a1cd3f721b1efdada1))
* Added support for Azure workload identity federation ([76ed673](https://github.com/googleapis/python-gke-multicloud/commit/76ed673d5438471fa90cf2a1cd3f721b1efdada1))

## [0.5.1](https://github.com/googleapis/python-gke-multicloud/compare/v0.5.0...v0.5.1) (2023-01-20)


### Bug Fixes

* Add context manager return types ([970b8d3](https://github.com/googleapis/python-gke-multicloud/commit/970b8d3a969d936e617d911de276816ec90a278a))


### Documentation

* Add documentation for enums ([970b8d3](https://github.com/googleapis/python-gke-multicloud/commit/970b8d3a969d936e617d911de276816ec90a278a))

## [0.5.0](https://github.com/googleapis/python-gke-multicloud/compare/v0.4.0...v0.5.0) (2023-01-12)


### Features

* Add support for python 3.11 ([#48](https://github.com/googleapis/python-gke-multicloud/issues/48)) ([e9ac58a](https://github.com/googleapis/python-gke-multicloud/commit/e9ac58ad64daa6ffdd0b346cbdff8a72a775908e))

## [0.4.0](https://github.com/googleapis/python-gke-multicloud/compare/v0.3.0...v0.4.0) (2023-01-04)


### Features

* Add AWS Autoscaling Group metrics collection for AWS nodepools ([3f1fa55](https://github.com/googleapis/python-gke-multicloud/commit/3f1fa55dcd74aa91dc4cf68302aa94720529e953))
* Add errors output fields for cluster and nodepool resources ([3f1fa55](https://github.com/googleapis/python-gke-multicloud/commit/3f1fa55dcd74aa91dc4cf68302aa94720529e953))
* Add monitoring config ([3f1fa55](https://github.com/googleapis/python-gke-multicloud/commit/3f1fa55dcd74aa91dc4cf68302aa94720529e953))
* Support AttachedClusters ([3f1fa55](https://github.com/googleapis/python-gke-multicloud/commit/3f1fa55dcd74aa91dc4cf68302aa94720529e953))

## [0.3.0](https://github.com/googleapis/python-gke-multicloud/compare/v0.2.2...v0.3.0) (2022-12-15)


### Features

* Add support for `google.cloud.gke_multicloud.__version__` ([de41e74](https://github.com/googleapis/python-gke-multicloud/commit/de41e74ea9308d01af05605d128d7feeea33b209))
* Add typing to proto.Message based class attributes ([de41e74](https://github.com/googleapis/python-gke-multicloud/commit/de41e74ea9308d01af05605d128d7feeea33b209))


### Bug Fixes

* Add dict typing for client_options ([de41e74](https://github.com/googleapis/python-gke-multicloud/commit/de41e74ea9308d01af05605d128d7feeea33b209))
* **deps:** Require google-api-core &gt;=1.34.0, >=2.11.0  ([71ad415](https://github.com/googleapis/python-gke-multicloud/commit/71ad41570864c1617ee6d4d5e33f07c037a8dba2))
* Drop usage of pkg_resources ([71ad415](https://github.com/googleapis/python-gke-multicloud/commit/71ad41570864c1617ee6d4d5e33f07c037a8dba2))
* Fix timeout default values ([71ad415](https://github.com/googleapis/python-gke-multicloud/commit/71ad41570864c1617ee6d4d5e33f07c037a8dba2))


### Documentation

* **samples:** Snippetgen handling of repeated enum field ([de41e74](https://github.com/googleapis/python-gke-multicloud/commit/de41e74ea9308d01af05605d128d7feeea33b209))
* **samples:** Snippetgen should call await on the operation coroutine before calling result ([71ad415](https://github.com/googleapis/python-gke-multicloud/commit/71ad41570864c1617ee6d4d5e33f07c037a8dba2))

## [0.2.2](https://github.com/googleapis/python-gke-multicloud/compare/v0.2.1...v0.2.2) (2022-10-10)


### Bug Fixes

* **deps:** Allow protobuf 3.19.5 ([#34](https://github.com/googleapis/python-gke-multicloud/issues/34)) ([36ffc90](https://github.com/googleapis/python-gke-multicloud/commit/36ffc90db52dfd0a90d26fd4c8c7bbac74269058))
* **deps:** require google-api-core&gt;=1.33.2 ([36ffc90](https://github.com/googleapis/python-gke-multicloud/commit/36ffc90db52dfd0a90d26fd4c8c7bbac74269058))

## [0.2.1](https://github.com/googleapis/python-gke-multicloud/compare/v0.2.0...v0.2.1) (2022-10-03)


### Bug Fixes

* **deps:** Require protobuf >= 3.20.2 ([#31](https://github.com/googleapis/python-gke-multicloud/issues/31)) ([8c73990](https://github.com/googleapis/python-gke-multicloud/commit/8c739901554b87048125d308ded429de4006b025))

## [0.2.0](https://github.com/googleapis/python-gke-multicloud/compare/v0.1.1...v0.2.0) (2022-09-16)


### Features

* Add support for REST transport ([#23](https://github.com/googleapis/python-gke-multicloud/issues/23)) ([763dbc4](https://github.com/googleapis/python-gke-multicloud/commit/763dbc4c4defe4888c815e7c8f6b42a6b8f63468))


### Bug Fixes

* **deps:** require google-api-core>=1.33.1,>=2.8.0 ([763dbc4](https://github.com/googleapis/python-gke-multicloud/commit/763dbc4c4defe4888c815e7c8f6b42a6b8f63468))
* **deps:** require protobuf >= 3.20.1 ([763dbc4](https://github.com/googleapis/python-gke-multicloud/commit/763dbc4c4defe4888c815e7c8f6b42a6b8f63468))

## [0.1.1](https://github.com/googleapis/python-gke-multicloud/compare/v0.1.0...v0.1.1) (2022-08-11)


### Bug Fixes

* **deps:** allow protobuf < 5.0.0 ([#10](https://github.com/googleapis/python-gke-multicloud/issues/10)) ([d5f33a6](https://github.com/googleapis/python-gke-multicloud/commit/d5f33a6c9a3ecfe6c8eb1feacefe367bf8b92afb))
* **deps:** require proto-plus >= 1.22.0 ([d5f33a6](https://github.com/googleapis/python-gke-multicloud/commit/d5f33a6c9a3ecfe6c8eb1feacefe367bf8b92afb))

## 0.1.0 (2022-07-08)


### Features

* generate v1 ([eb3bd85](https://github.com/googleapis/python-gke-multicloud/commit/eb3bd8516f44889a652422961d38aa5cf4352074))
