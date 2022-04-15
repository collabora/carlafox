import nbdev.clean as nbclean
import io, sys, json

fname = sys.argv[1]

# load the notebook
nb = json.loads(open(fname, 'r', encoding='utf-8').read())
# do a standard nbdev clean
nbclean.clean_nb(nb, clear_all=False)
# remove outputs (except for the #keep-output cells)
for c in nb['cells']:
    if c['source'][0] != '#keep-output\n':
        if 'outputs' in c: c['outputs'] = []
# save the notebook
x = json.dumps(nb, sort_keys=True, indent=1, ensure_ascii=False)
with io.open(fname, 'w', encoding='utf-8') as f:
    f.write(x)
    f.write("\n")
