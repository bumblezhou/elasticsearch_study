from datetime import datetime
from elasticsearch import Elasticsearch

# Replace these with your actual username and password
username = 'elastic'
password = 'usKuJ3daCL4vf98kQ0Dk'

# Create the connection instance
es = Elasticsearch(
    ['http://localhost:9200'],
    basic_auth=(username, password)
)

doc_1 = {
    'ContractName': 'Elementary school rebuilding',
    'ContractContent': 'The ceremony marks the beginning of construction at the $125 million project, which includes new construction of approximately 81,000 square feet and extensive renovations of 68,094 square feet to the existing building. The project also includes new furnishings and playground improvements. When complete, Bechtel Elementary will feature student-centered design elements including neighborhood instructional spaces and furnishings that support collaboration and community.During construction, Bechtel Elementary will continue to operate out of Kadena Elementary (Universal Prekindergarten, Kindergarten, and Preschool Services for Children with Disabilities) and Ryukyu Middle (grades 1-5). DoDEA plans, directs, coordinates, and manages Pre-Kindergarten through 12th grade education programs for school-aged children of Department of Defense personnel who would otherwise not have access to a high-quality public education. DoDEA schools are located in Europe, the Pacific, Western Asia, the Middle East, Cuba, the United States, Guam, and Puerto Rico. DoDEA also provides support and resources to Local Educational Activities throughout the U.S. that serve children of military families.',
    'AssociatedEmail': 'taro@example.com',
    'PublishDate': '2010-01-24',
    'ProjectName': 'Elementary school rebuilding',
    'AssociatedUnits': 'X distrit gov, A building company'
}

doc_2 = {
    'ContractName': 'Swimming pool rebuilding',
    'ContractContent': 'An outdoor swimming pool will be exposed to the elements and so they require plenty of care to keep them in good condition. The ground around your pool has the potential to shrink and expand, which can exacerbate any issues you may face over time. Whether you’ve had your pool for a long time or you’ve moved into a property that already had one, there are some common signs that it may be time to update it. The first is cracks in the structure of the pool. While this may be alarming to see, there are varying levels of damage that could be at play, and the placement and size of the damage will determine the scale of the issue. Surface level cracks in the concrete are known as craze cracks and while they may lead to other problems if they’re left to develop, they’re not necessarily a reason to immediately refurbish. But structural cracks are a bigger problem and can be costly to fix.',
    'AssociatedEmail': 'taro@example.com',
    'PublishDate': '2010-01-24',
    'ProjectName': 'Swimming pool rebuilding',
    'AssociatedUnits': 'C distrit Swimming pool, B building company'
}

doc_3 = {
    'ContractName': 'Library Renovation',
    'ContractContent': 'The purpose of library renovation can vary depending on the specific goals and needs of the library and its patrons. However, in general, library renovation is intended to improve the functionality, accessibility, and aesthetic appeal of the library in order to better serve the community and meet the changing needs of library users. Some specific goals of library renovation may include: 1. Updating and modernizing the library’s technology and equipment, such as computers, printers, and audiovisual systems. 2. Improving the library’s layout and space utilization to create a more efficient and comfortable environment for users, such as adding collaborative workspaces or quiet study areas. 3. Enhancing the library’s accessibility for people with disabilities, such as by installing ramps, elevators, or assistive technology. 4. Adding new amenities and services to the library, such as cafes, maker spaces, or specialized collections. 5. Upgrading the library’s infrastructure and systems, such as HVAC or lighting, to improve energy efficiency and sustainability. 6. Refreshing the library’s decor and furnishings to create a more inviting and attractive space for users.',
    'AssociatedEmail': 'taro@example.com',
    'PublishDate': '2010-01-24',
    'ProjectName': 'Library Renovation',
    'AssociatedUnits': 'X City Library, C building company'
}

# Create indices
if es.indices.exists(index="documents"):
    es.indices.delete(index="documents")
else:
    es.indices.create(index='documents')

# Insert docs
res = es.index(index="documents", id=1, document=doc_1)
res = es.index(index="documents", id=2, document=doc_2)
res = es.index(index="documents", id=3, document=doc_3)

# Get doc
res = es.get(index="documents", id=1)
print(res['_source'])
res = es.get(index="documents", id=2)
print(res['_source'])
res = es.get(index="documents", id=3)
print(res['_source'])

# Refreseh index
es.indices.refresh(index="documents")

# Search:
# res = es.search(index="documents", query={"match_all": {}})
res = es.search(index="documents", query={"bool": {"should": [{"match": {"ContractContent": "renovation"}}, {"match": {"AssociatedUnits": "Library"}}]}})
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print("%(ProjectName)s: %(ContractName)s %(PublishDate)s" % hit["_source"])