# Location: `sky/backends/cloud_vm_ray_backend.py`
...
 def _update_blocklist_on_fluffycloud_error(
            self, launchable_resources: 'resources_lib.Resources', region,
            zones, stdout, stderr):
        del zones  # Unused.
        style = colorama.Style
        stdout_splits = stdout.split('\n')
        stderr_splits = stderr.split('\n')
        errors = [
            s.strip()
            for s in stdout_splits + stderr_splits
            if 'FluffyCloudError:' in s.strip()
        ]
        if not errors:
            logger.info('====== stdout ======')
            for s in stdout_splits:
                print(s)
            logger.info('====== stderr ======')
            for s in stderr_splits:
                print(s)
            with ux_utils.print_exception_no_traceback():
                raise RuntimeError('Errors occurred during provision; '
                                   'check logs above.')

        logger.warning(f'Got error(s) in {region.name}:')
        messages = '\n\t'.join(errors)
        logger.warning(f'{style.DIM}\t{messages}{style.RESET_ALL}')
        self._blocked_resources.add(launchable_resources.copy(zone=None))
...
def _update_blocklist_on_error(
    ...
    handlers = {
        ...
        # TODO Add this
        clouds.fluffycloud: self._update_blocklist_on_fluffycloud_error,
        ...
    }
    ...
...
def _yield_region_zones(self, to_provision: resources_lib.Resources,
                        cluster_name: str, cluster_exists: bool):
    ...
            elif cloud.is_same_cloud(clouds.Azure()):
                                region = config['provider']['location']
                                zones = None
            # TODO Add this
            elif cloud.is_same_cloud(clouds.FluffyCloud()):
                                region = config['provider']['location']
                                zones = None
    ...
...
