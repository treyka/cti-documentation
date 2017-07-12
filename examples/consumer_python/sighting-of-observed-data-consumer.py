import stix2

for obj in bundle.objects:
    if obj == identityPym:
        print("------------------")
        print("== IDENTITY ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Name: " + obj.name)
        print("Identity Class: " + obj.identity_class)
        print("Contact Information: " + obj.contact_information)
        print("Sectors: " + obj.sectors[0])

    elif obj == identityOscorp:
        print("------------------")
        print("== IDENTITY ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Name: " + obj.name)
        print("Identity Class: " + obj.identity_class)
        print("Contact Information: " + obj.contact_information)
        print("Sectors: " + obj.sectors[0])

    elif obj == malware:
        print("------------------")
        print("== MALWARE ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Created by Ref: " + obj.created_by_ref)
        print("Name: " + obj.name)
        print("Description: " + obj.description)
        print("Labels: " + obj.labels[0])

    elif obj == observedDataFile:
        print("------------------")
        print("== OBSERVED DATA ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Created by Ref: " + obj.created_by_ref)
        print("First Observed: " + str(obj.first_observed))
        print("Last Observed: " + str(obj.last_observed))
        print("Number Observed: " + str(obj.number_observed))
        print("Objects: " + str(obj.objects))

    elif obj == observedDataRegKey:
        print("------------------")
        print("== OBSERVED DATA ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Created by Ref: " + obj.created_by_ref)
        print("First Observed: " + str(obj.first_observed))
        print("Last Observed: " + str(obj.last_observed))
        print("Number Observed: " + str(obj.number_observed))
        print("Objects: " + str(obj.objects))

    elif obj == sighting:
        print("------------------")
        print("== SIGHTING ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Created by Ref: " + obj.created_by_ref)
        print("First Seen: " + str(obj.first_seen))
        print("Last Seen: " + str(obj.last_seen))
        print("Count: " + str(obj.count))
        print("Sighting of Ref: " + obj.sighting_of_ref)
        print("Where Sighted Refs: " + obj.where_sighted_refs[0])
