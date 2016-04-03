private String calculateHMac(Request paramRequest, String paramString) {
	try {
		/* This may be either the complete request URL or a partial URL.
		 * Not known as of yet due to obfuscation. */
		URI localURI = paramRequest.BT();

		/* Create a StringBuilder and initialise it to the HTTP method.
		 * paramRequest.Cw() may be "GET", "POST", "PUT", etc. */
		StringBuilder localStringBuilder = new StringBuilder(paramRequest.Cw());

		/* Append some information about the request separated by '%' signs. */
		localStringBuilder
			.append("%")
			.append(localURI.getHost())        /* "api.go-tellm.com" */
			.append("%")
			.append(String.valueOf(this.port)) /* "443" */
			.append("%")
			.append(localURI.getPath())        /* "/api/v2/users/" */
			.append("%");

		/* Try to get the "Authorization" header from the request. */
		String str = paramRequest.dn("Authorization");

		/* Append the contents of the "Authorization" header if it was found. */
		if (!TextUtils.isEmpty(str)) {
			localStringBuilder.append(str.split(" ")[1]);
		}
		/* Append the current time formatted as ISO 8601 with the offset from UTC.
		 *   - Format : "YYYY-MM-DDTHH:MM:SSZ"
		 *   - Example: "2016-04-03T13:12:38Z" */
		localStringBuilder
			.append("%")
			.append(paramString);

		appendQuery(localStringBuilder, localURI.getQuery());
		appendBody(localStringBuilder, paramRequest);
		paramRequest = localStringBuilder.toString();
		paramString = Mac.getInstance("HmacSHA1");
		paramString.init(new SecretKeySpec(this.secret, "HmacSHA1"));
		paramRequest = hex(paramString.doFinal(paramRequest.getBytes("UTF-8")));

		return paramRequest;
	} catch (Throwable paramRequest) {
		Crashlytics.logException(paramRequest);
	}

	return "";
}
