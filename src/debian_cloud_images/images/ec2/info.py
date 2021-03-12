from ..publicinfo import ImagePublicInfo
from ...utils.libcloud.compute.ec2 import ExEC2NodeDriver
from ...utils.libcloud.storage.s3 import S3BucketStorageDriver


class Ec2Info:
    noop: bool
    public: ImagePublicInfo
    drivers_compute: dict[str, ExEC2NodeDriver]
    driver_storage: S3BucketStorageDriver

    def __init__(
        self,
        noop: bool,
        public: ImagePublicInfo,
        drivers_compute: dict[str, ExEC2NodeDriver],
        driver_storage: S3BucketStorageDriver,
    ) -> None:
        self.noop = noop
        self.public = public
        self.drivers_compute = drivers_compute
        self.driver_storage = driver_storage