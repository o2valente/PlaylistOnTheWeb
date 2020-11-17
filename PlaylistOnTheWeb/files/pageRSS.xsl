<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="rss">
        <xsl:for-each select="channel">

            <xsl:for-each select="item">
                <ul id="card">
                <ul>
                    <li>
                    <p>
                    <u><i>TITLE:</i></u><xsl:text>  </xsl:text>
                    <xsl:value-of select="title"/> <br />
                    </p>
                    <p>
                    <u><i>DATE:</i></u><xsl:text>  </xsl:text>
                    <xsl:value-of select="pubDate"/>  <br />
                    </p>
                    <p>
                    <u><i>DESCRIPTION:</i></u><xsl:text>  </xsl:text>
                    <xsl:value-of select="description"/> <br />
                    </p>
                    <p>
                    <u><i>LINK:</i></u><xsl:text>  </xsl:text>
                    <xsl:variable name="link" select="link"/>
                    <a style="color:white;" href="{link}" target="_blank">
                    <xsl:value-of select="link"/></a>  <br />
                    </p>
                    </li>
                </ul>
                </ul>
            </xsl:for-each>

            <br /><br />
        </xsl:for-each>

    </xsl:template>
</xsl:stylesheet>