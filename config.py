# ids for workflow, project and inputs
projectID = "project-Fy9G62Q4gk5784zB9xPpVFJ1"
workflowID = "workflow-Fy8qkxQ433GV4kQv4z8YJ0p0"

# define inputs for each stage of workflow
inputs = {
    "0.genomebwaindex_targz": {
        '$dnanexus_link': {
            'project': 'project-F3zxk7Q4F30Xp8fG69K1Vppj',
            'id': 'file-F404y604F30fbxQG68KF3GZb'
        }
    },
    "0.genome_fastagz": {
        '$dnanexus_link': 'file-F403K904F30y2vpVFqxB9kz7'
    },
    "0.reads_fastqgzs": [
        {'$dnanexus_link': {
            'project': 'project-FxbQ20Q4xq8gxY9x6vkZqZ7F',
            'id': 'file-Fxb69184X7kv15p05jKx01P5'
        }},
        {'$dnanexus_link': {
            'project': 'project-FxbQ20Q4xq8gxY9x6vkZqZ7F',
            'id': 'file-Fxb691Q4X7kb53Gp2xXQYX41'
        }}
    ],
    "0.reads2_fastqgzs": [
        {'$dnanexus_link': {
            'project': 'project-FxbQ20Q4xq8gxY9x6vkZqZ7F',
            'id': 'file-Fxb69x04X7kkQgKq8ZqY4F3f'
        }},
        {'$dnanexus_link': {
            'project': 'project-FxbQ20Q4xq8gxY9x6vkZqZ7F',
            'id': 'file-Fxb697j4X7kzQvby05JQGgvj'
        }}
    ],
    "1.query_vcf": {'$dnanexus_link': {
        'stage': 'stage-Fy8qp6Q433Gk1p7jF3493gqb',
        'outputField': 'variants_vcf'
    }},
    "1.truth_vcf": {'$dnanexus_link': {
        'stage': 'stage-Fy8qp6Q433Gk1p7jF3493gqb',
        'outputField': 'variants_vcf'
    }}
}
