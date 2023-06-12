# Postman-Api-Count

Postman-API-Count is a powerful tool designed to facilitate the extraction and analysis of APIs from Postman collections. It provides various functionalities to help users extract APIs with specific HTTP methods or without any methods defined. Additionally, it allows for the retrieval of the total count of APIs within a collection.

The tool is particularly useful for developers, testers, and API enthusiasts who work with Postman collections and need to gather information about the APIs contained within them. By leveraging Postman-API-Count, users can streamline their workflow and gain insights into the structure and characteristics of their API collections.

Key features of Postman-API-Count include:

1. API Extraction: The tool enables users to extract APIs based on specific HTTP methods. This means you can easily filter and retrieve APIs that are GET, POST, PUT, DELETE, or any other HTTP verb.

2. Extraction of APIs without Methods: In addition to extracting APIs based on methods, Postman-API-Count allows users to identify APIs that do not have any methods defined. This can be particularly useful for identifying incomplete or unfinished APIs within a collection.

3. Total API Count: The tool offers a straightforward way to obtain the total count of APIs in a Postman collection. By simply running the count command, users can quickly gather information about the number of APIs they have in their collection.

By leveraging Postman-API-Count, developers and testers can streamline their API management processes, gain insights into their collections, and improve the overall quality and efficiency of their API development workflows.

# Uses

     git clone https://github.com/pentesterhelper/Postman-Api-Count.git
     cd Postman-API-Count
     
     Without Method
     
     Request -> python3 PostmanAPICount.py filename.postmancollection.json
     Response -> https://pentesterhelper.cloud/api/login
                 https://pentesterhelper.cloud/api/forgetpassword
                 https://pentesterhelper.cloud/api/commanId/879
                 https://pentesterhelper.cloud/api/upload/user/789
                 Total API:  4
                 
     With Method
     
     Request -> python3 PostmanAPICount.py filename.postmancollection.json --method
     Response -> POST : https://pentesterhelper.cloud/api/login
                 POST : https://pentesterhelper.cloud/api/forgetpassword
                 GET :  https://pentesterhelper.cloud/api/commanId/879
                 GET :  https://pentesterhelper.cloud/api/upload/user/789
                 Total API:  4
    
    
