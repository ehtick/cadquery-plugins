import cadquery as cq
import cadquery
from plugins.cq_cache.cq_cache import cq_cache, clear_cq_cache, get_cache_dir_size
import tempfile
import os

TEMPDIR_PATH = tempfile.gettempdir()
CACHE_DIR_NAME = "cadquery_geom_cache"
CACHE_DIR_PATH = os.path.join(TEMPDIR_PATH,CACHE_DIR_NAME)
CACHE_SIZE = 0.1

@cq_cache(CACHE_SIZE)
def cube(a,b,c):
    cube = cq.Workplane().box(a,b,c)
    return cube.val()

def test_get_cache_dir_size():
    with open(os.path.join(CACHE_DIR_PATH,"fill.txt"), "w") as f:
        f.write("test") 
    assert get_cache_dir_size(CACHE_DIR_PATH) == 4

def test_clear_cache():
    with open(os.path.join(CACHE_DIR_PATH,"fill.txt"), "w") as f:
        f.write("test")
    assert len(os.listdir(CACHE_DIR_PATH)) == 1
    clear_cq_cache()
    assert len(os.listdir(CACHE_DIR_PATH)) == 0

def test_cache_file_creation():
    clear_cq_cache()
    cube1 = cube(1,1,1)
    cube2 = cube(1,1,1)
    files = os.listdir(CACHE_DIR_PATH)
    assert len(files) == 1
    assert files[0] == "cube_1_1_1.step"

def test_not_exceeding_size():
    clear_cq_cache()
    for i in range(20):
        cube(1,1,1+i)
    assert get_cache_dir_size(CACHE_DIR_PATH) < CACHE_SIZE*1e6

# def test_cache_type_return():
#     cube1 = cube(1,1,1)
#     cube2 = cube(1,1,1)
#     print(type(cube1))
#     assert isinstance(cube1,cadquery.occ_impl.shapes.Solid)



