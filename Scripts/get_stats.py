import sys
from io import StringIO
from pprint import pprint

import gpustat


def get_stats():
    # gpustat.print_gpustat(show_pid=True, show_cmd=True)
    stats = {}
    parsed_processes = {}
    gpu_stats = gpustat.GPUStatCollection.new_query(debug=False)
    json = gpu_stats.jsonify()
    info = json['gpus'][0]
    # pprint(info)
    stats['id'] = str(info['index'])
    stats['name'] = info['name']
    stats['usage'] = str(info['utilization.gpu']) + '%'
    processes = info['processes']
    for p in processes:
        process_name = p['command']
        pid = str(p['pid'])
        parsed_processes[process_name] = pid
    stats['processes'] = parsed_processes
    return stats


if __name__ == '__main__':
    stats = get_stats()