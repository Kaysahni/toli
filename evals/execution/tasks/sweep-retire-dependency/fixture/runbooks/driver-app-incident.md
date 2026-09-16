# Driver app: drivers cannot submit proof of delivery

Owner: Mobile team

Symptoms: drivers report a spinner after taking the photo; support tickets
mention "stuck on upload".

Check in this order:

1. pod-uploader error rate (Grafana "Mobile / POD"). Above 2%? Go to 4.
2. Is the driver on an app version below MIN_SUPPORTED_APP_VERSION? Support can
   see this in the driver profile. Ask them to update.
3. Is it one depot? Depot Wi-Fi in HSK has failed twice this year. The app
   retries on mobile data only if the driver allowed it.
4. Check the virus scanner. If clamav pods are restarting, uploads time out.
   Scale clamav to 3 and page Platform Security.
5. Still broken: page Mobile on-call. The app queues PODs locally for 72 hours,
   so there is no data loss as long as it is fixed within that window.
