from unittest import TestCase
from src.collaboratory import Collaboratory


class TestCollaboratory(TestCase):

    def setUp(self):
        self.database = Collaboratory.default_init()
        self.start_date = "2016-08-01T00:00:00"
        self.end_date = "2016-09-01T00:00:00"
        self.project_id = "8e95a3bd98bb4560a12a0dc6d9f265e4"
        self.user_1 = "19f5e963e6e1429897ecabb52f958c2f"

    def tearDown(self):
        self.database.database.close()

    def test_get_instance_core_hours_by_user(self):
        self.assertEqual(self.database.get_instance_core_hours_by_user(self.start_date,
                                                                       self.end_date,
                                                                       self.project_id,
                                                                       self.user_1),
                         34012)

    def test_get_volume_gigabyte_hours_by_user(self):
        self.assertEqual(self.database.get_volume_gigabyte_hours_by_user(self.start_date,
                                                                         self.end_date,
                                                                         self.project_id,
                                                                         self.user_1),
                         409760)

''' Test Data located at mysql://root:test@142.1.177.124:3306
nova.instances:
  user_id: 19f5e963e6e1429897ecabb52f958c2f
    created_at = 2010-01-01             96      hours
    deleted_at = 2016-08-05             96      core_hours
    cores      = 1

    created_at = 2016-07-30             12      hours
    deleted_at = 2016-08-01 12:00:00    24      core_hours
    cores      = 2

    created_at = 1990-01-01             744     hours
    deleted_at = NULL                   2976    core_hours
    cores      = 4

    created_at = 2016-04-01             744     hours
    deleted_at = 2016-09-02             5952    core_hours
    cores      = 8

    created_at = 2016-08-03             408     hours
    deleted_at = 2016-08-20             3264    core_hours
    cores      = 8

    created_at = 2016-08-24             192     hours
    deleted_at = 2020-01-04             192     core_hours
    cores      = 1

    created_at = 2016-08-16             384     hours
    deleted_at = NULL                   768     core_hours
    cores      = 2

    created_at = 2016-08-29 00:00:00    1       hours
    deleted_at = 2016-08-29 00:00:01    4       core_hours
    cores      = 4

    created_at = 2016-07-09             0       hours
    deleted_at = 2016-07-20             0       core_hours
    cores      = 600

    created_at = 2016-09-01             0       hours
    deleted_at = NULL                   0       core_hours
    cores      = 30

    created_at = 2016-08-01             144     hours
    created_at = 2016-08-07             2304    core_hours
    cores      = 16

    created_at = 2016-08-08             576     hours
    deleted_at = 2016-09-01             18432   core_hours
    cores      = 32
                                        34012   total core_hours
  user_id: ee5cd68120c84c16b16f870915b9e654


cinder.volumes:
  user_id: 19f5e963e6e1429897ecabb52f958c2f
    created_at = 2016-06-23             81      hours
    deleted_at = 2016-08-04 08:03:12    6480    GB_hours
    size       = 80

    created_at = 2016-02-04 23:59:59    72      hours
    deleted_at = 2016-08-03 23:59:59    23040   GB_hours
    size       = 320

    created_at = 1867-07-01             744     hours
    deleted_at = 2040-09-04             59520   GB_hours
    size       = 80

    created_at = 2016-08-01 00:00:01    24      hours
    deleted_at = 2016-08-02             1920    GB_hours
    size       = 80

    created_at = 2016-08-21 13:08:23    5       hours
    deleted_at = 2016-08-21 17:41:52    400     GB_hours
    size       = 80

    created_at = 2016-08-03             48      hours
    deleted_at = 2016-08-05             3840    GB_hours
    size       = 80

    created_at = 2016-08-01 00:52:01    744     hours
    deleted_at = 2016-09-01 00:00:01    59520   GB_hours
    size       = 80

    created_at = 2016-08-31 23:59:59    1       hours
    deleted_at = 2016-09-01             1000    GB_hours
    size       = 1000

    created_at = 2016-04-21             0       hours
    deleted_at = 2016-08-01             0       GB_hours
    size       = 160

    created_at = 2016-09-01             0       hours
    deleted_at = 2016-10-04             0       GB_hours
    size       = 600

    created_at = 2016-08-14 15:02:23    417     hours
    deleted_at = 2016-10-22             250200  GB_hours
    size       = 600

    created_at = 2016-08-30             48      hours
    deleted_at = NULL                   3840    GB_hours
    size       = 80
                                        409760  total GB_hours
  user_id: ee5cd68120c84c16b16f870915b9e654

glance.images
  owner: 8e95a3bd98bb4560a12a0dc6d9f265e4
'''