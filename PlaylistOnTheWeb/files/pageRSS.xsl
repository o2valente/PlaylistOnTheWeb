<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="root">
        <xsl:for-each select="playlistDemo">
            <xsl:value-of select="title"/>
            <xsl:for-each select="item">
                <u><i>TITLE: </i></u>
                <xsl:value-of select="title"/> <br />
                <u><i>LINK: </i></u>
                <xsl:value-of select="link"/>  <br />
                <u><i>DATE: </i></u>
                <xsl:value-of select="pubDate"/>  <br />
                <u><i>New: </i></u>
                <xsl:value-of select="description"/> <br />
            </xsl:for-each>
            <br /><br />
        </xsl:for-each>

    </xsl:template>
</xsl:stylesheet>