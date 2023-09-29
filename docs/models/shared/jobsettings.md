# JobSettings


## Fields

| Field                            | Type                             | Required                         | Description                      |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `concurrent_job_limit`           | *Optional[int]*                  | :heavy_check_mark:               | N/A                              |
| `concurrent_scheduled_job_limit` | *Optional[int]*                  | :heavy_check_mark:               | N/A                              |
| `concurrent_system_job_limit`    | *Optional[int]*                  | :heavy_check_mark:               | N/A                              |
| `concurrent_system_task_limit`   | *Optional[int]*                  | :heavy_check_mark:               | N/A                              |
| `concurrent_task_limit`          | *Optional[int]*                  | :heavy_check_mark:               | N/A                              |
| `finished_job_artifacts_limit`   | *Optional[int]*                  | :heavy_check_mark:               | N/A                              |
| `finished_task_artifacts_limit`  | *Optional[int]*                  | :heavy_check_mark:               | N/A                              |
| `job_artifacts_reaper_period`    | *Optional[str]*                  | :heavy_check_mark:               | N/A                              |
| `job_timeout`                    | *Optional[str]*                  | :heavy_check_mark:               | N/A                              |
| `max_task_perc`                  | *Optional[int]*                  | :heavy_check_mark:               | N/A                              |
| `scheduling_policy`              | *Optional[str]*                  | :heavy_check_mark:               | N/A                              |
| `task_heartbeat_period`          | *Optional[int]*                  | :heavy_check_mark:               | N/A                              |
| `task_manifest_flush_period_ms`  | *Optional[int]*                  | :heavy_check_mark:               | N/A                              |
| `task_manifest_max_buffer_size`  | *Optional[int]*                  | :heavy_check_mark:               | N/A                              |
| `task_manifest_read_buffer_size` | *Optional[str]*                  | :heavy_check_mark:               | N/A                              |
| `task_poll_timeout_ms`           | *Optional[int]*                  | :heavy_check_mark:               | N/A                              |