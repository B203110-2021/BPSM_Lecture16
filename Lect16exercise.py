import os, sys, re, numpy as np
import pandas as pd
os.system("wget -qO eukaryotes.tsv 'ftp://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/eukaryotes.txt'")
df = pd.read_csv('eukaryotes.tsv', sep="\t", na_values=['-'])
df.index=df.apply(lambda x : "{} ({})".format(x['#Organism/Name'], x['BioSample Accession']), axis=1)
len( df[ (df['Group'] == 'Fungi') & (df['Size (Mb)'] > 100) ] )
len(df[df.apply(lambda x : x['Group'] == 'Fungi' and x['Size (Mb)'] > 100, axis=1)])
big_fungi = df[(df['Group'] == 'Fungi') & (df['Size (Mb)'] > 100)]
list(big_fungi['#Organism/Name'])
sorted(list(big_fungi['#Organism/Name']))
len(df[df['Group'] == 'Plants'])
len(df[df['Group'].str.lower() == 'plants'])
for Group in ['Plants', 'Animals', 'Fungi', 'Protists']:
    count = len(df[df['Group'] == Group])
    count_unique = len(df[df['Group'] == Group].drop_duplicates('#Organism/Name'))
    print("{} genomes for {} ({} unique)".format(count, Group, count_unique))
hel = df[df.apply(lambda x : x['#Organism/Name'].startswith('Heliconius'), axis=1)]
hel[ ['#Organism/Name', 'Scaffolds'] ]
df[df['Group'] == 'Plants']['Center'].value_counts().head()
df[df['SubGroup'] == 'Insects']['Center'].value_counts().head()
df['Proteins per gene'] = df['Proteins'] / df['Genes']
df[ ['#Organism/Name', 'Group', 'Proteins per gene'] ].head()
df[df['Proteins per gene'] >= 1.1][ ['#Organism/Name', 'Genes','Proteins','Proteins per gene'] ].head()
len(df[df['Proteins per gene'] >= 1.1][ ['#Organism/Name', 'Genes','Proteins','Proteins per gene'] ])
