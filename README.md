 # MYRESTAPP
simple api making use of twitter feeds and the created with the django rest framework
```
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python mange.py runserver```

EndPoints
```127.0.0.1:8000/api/v1/trends
127.0.0.1:8000/api/v1/trends/:id
```
scraping data with the twiiter api
```127.0.0.1:8000/scraptweets```


=== Jump Host Access ===

{| class="wikitable"
! GUI Access
! Source
! Destination
! Port
! Type of Change
! Devices Involved
! Ticket Info
|----
|Jump Host Access
|10.247.156.0/22
|10.239.0.0/16
|any
|FW Rule
|FW1/2.COLO-BO.BRN1/ILG1
|
|----
|Jump access to ServiceNow external addresses
|10.171.164.101,  10.171.164.97
|199.91.140.100,  199.91.136.100
|TCP 80,  443
|FW
|fw.shared-bo.brn1
|CHG105805
|----
|Jump access to ServiceNow external addresses
|10.247.164.101,  10.247.164.97
|199.91.140.100,  199.91.136.100
|TCP 80,  443
|FW
|vpn1/2.shared-bo.ilg1
|CHG105805
|----
|}

