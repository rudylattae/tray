import os
import bottle
from bottle import static_file
from bottle.ext.servefiles import BottleStaticFileBucket
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
            BottleStaticFileBucket(config)
            raise AssertionError('Expected "ValueError" to be raised')
        except ValueError as ex:
            assert ex.message == expected_message

    @fudge.patch('os.path.exists')
    def it_sets_the_root_dir_if_it_is_valid(self, mock_path_exists):
        config = {'ROOT_DIR': '/valid/path'}
        mock_path_exists.expects_call() \
            .with_args(config['ROOT_DIR']) \
            .returns(True)
        
        repo = BottleStaticFileBucket(config)
        
        assert repo.root_dir == config['ROOT_DIR']


class describe_get:
    @fudge.patch('os.path.exists', 'bottle.static_file')
    def it_delegates_to_bottle_to_serve_the_requested_file_if_it_exists(self, mock_path_exists, mock_bottle_staticfile):
        config = {'ROOT_DIR': '/valid/path'}
        expected_filename = 'my_file.txt'
        mock_path_exists.expects_call() \
            .with_args(config['ROOT_DIR']) \
            .returns(True)
        mock_bottle_staticfile.is_callable().expects_call() \
            .with_args(expected_filename, root=config['ROOT_DIR']) \
            .returns("")
        repo = BottleStaticFileBucket(config)
        
        repo.get(expected_filename)

