private String calculateHMac(Request paramRequest, String paramString) {
	try {
		URI localURI = paramRequest.BT();
		StringBuilder localStringBuilder = new StringBuilder(paramRequest.Cw());

		localStringBuilder
			.append("%")
			.append(localURI.getHost())
			.append("%")
			.append(String.valueOf(this.port))
			.append("%")
			.append(localURI.getPath())
			.append("%");

		/* Try to get the "Authorization" header from the request. */
		String str = paramRequest.dn("Authorization");

		/* Append the "Authorization" header if it was found.  */
		if (!TextUtils.isEmpty(str)) {
			localStringBuilder.append(str.split(" ")[1]);
		}
		/* Append the current time formatted as ISO 8601 with the offset from UTC.*/
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
