import os

from setuptools import find_packages, setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension


def make_cuda_ext(name, module, sources):
    cuda_ext = CUDAExtension(
        name='%s.%s' % (module, name),
        sources=[os.path.join(*module.split('.'), src) for src in sources]
    )
    return cuda_ext


setup(
    name='mydetector3d',
    cmdclass={'build_ext': BuildExtension},
    ext_modules=[
            make_cuda_ext(
                name="bev_pool_ext",
                module="mydetector3d.ops.bev_pool",
                sources=[
                    "src/bev_pool.cpp",
                    "src/bev_pool_cuda.cu",
                    ],
            ),
            make_cuda_ext(
                name='iou3d_nms_cuda',
                module='mydetector3d.ops.iou3d_nms',
                sources=[
                    'src/iou3d_cpu.cpp',
                    'src/iou3d_nms_api.cpp',
                    'src/iou3d_nms.cpp',
                    'src/iou3d_nms_kernel.cu',
                ]
            ),
            make_cuda_ext(
                name='roiaware_pool3d_cuda',
                module='mydetector3d.ops.roiaware_pool3d',
                sources=[
                    'src/roiaware_pool3d.cpp',
                    'src/roiaware_pool3d_kernel.cu',
                ]
            ),
            make_cuda_ext(
                name='roipoint_pool3d_cuda',
                module='mydetector3d.ops.roipoint_pool3d',
                sources=[
                    'src/roipoint_pool3d.cpp',
                    'src/roipoint_pool3d_kernel.cu',
                ]
            ),
            make_cuda_ext(
                name='pointnet2_stack_cuda',
                module='mydetector3d.ops.pointnet2.pointnet2_stack',
                sources=[
                    'src/pointnet2_api.cpp',
                    'src/ball_query.cpp',
                    'src/ball_query_gpu.cu',
                    'src/group_points.cpp',
                    'src/group_points_gpu.cu',
                    'src/sampling.cpp',
                    'src/sampling_gpu.cu', 
                    'src/interpolate.cpp', 
                    'src/interpolate_gpu.cu',
                    'src/voxel_query.cpp', 
                    'src/voxel_query_gpu.cu',
                    'src/vector_pool.cpp',
                    'src/vector_pool_gpu.cu'
                ],
            ),
            make_cuda_ext(
                name='pointnet2_batch_cuda',
                module='mydetector3d.ops.pointnet2.pointnet2_batch',
                sources=[
                    'src/pointnet2_api.cpp',
                    'src/ball_query.cpp',
                    'src/ball_query_gpu.cu',
                    'src/group_points.cpp',
                    'src/group_points_gpu.cu',
                    'src/interpolate.cpp',
                    'src/interpolate_gpu.cu',
                    'src/sampling.cpp',
                    'src/sampling_gpu.cu',

                ],
            ),
        ]

)