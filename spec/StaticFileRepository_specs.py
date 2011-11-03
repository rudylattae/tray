from bottle.ext.servefiles import StaticFileRepository
import fudge


class describe_creating_an_instance:
    @fudge.patch('os.path.exists')
    def it_blows_up_if_the_provided_root_dir_is_invalid(self, mock_path_exists):
        config = {'ROOT_DIR': '/non/existent/path'}
        expected_message = 'Root directory %s not found' % config['ROOT_DIR']
        mock_path_exists.expects_call() \
            .with_args(config['ROOT_DIR']) \
            .returns(False)
            
        try:
            StaticFileRepository(config)
            raise AssertionError('Expected "ValueError" to be raised')
        except ValueError as ex:
            assert ex.message == expected_message

    @fudge.patch('os.path.exists')
    def it_sets_the_root_dir_if_it_is_valid(self, mock_path_exists):
        config = {'ROOT_DIR': '/valid/path'}
        mock_path_exists.expects_call() \
            .with_args(config['ROOT_DIR']) \
            .returns(True)
        
        repo = StaticFileRepository(config)
        
        assert repo.root_dir == config['ROOT_DIR']
