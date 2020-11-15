<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="rss">
        <xsl:for-each select="channel">

            <xsl:for-each select="item">
                <ul>
                    <li>
                    <u><i>TITLE:</i></u><xsl:text>  </xsl:text>
                    <xsl:value-of select="title"/> <br />
                    </li>
                    <li>
                    <u><i>DATE:</i></u><xsl:text>  </xsl:text>
                    <xsl:value-of select="pubDate"/>  <br />
                    </li>
                    <li>
                    <u><i>DESCRIPTION:</i></u><xsl:text>  </xsl:text>
                    <xsl:value-of select="description"/> <br />
                    </li>
                    <li>
                    <u><i>LINK:</i></u><xsl:text>  </xsl:text>
                    <xsl:variable name="link" select="link"/>
                    <a style="color:#A4CA55;" href="{link}" target="_blank">
                    <xsl:value-of select="link"/></a>  <br />
                    </li>
                </ul>
            </xsl:for-each>

            <br /><br />
        </xsl:for-each>

    </xsl:template>
</xsl:stylesheet>