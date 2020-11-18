<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="rss">
        <xsl:for-each select="channel">

            <xsl:for-each select="item">
                <ul id="card" class="five">
                <ul>
                    <li>
                    <p>
                    <strong><i>TITLE:</i></strong><xsl:text>  </xsl:text>
                    <xsl:value-of select="title"/> <br />
                    </p>
                    <p>
                    <strong><i>DATE:</i></strong><xsl:text>  </xsl:text>
                    <xsl:value-of select="pubDate"/>  <br />
                    </p>
                    <p>
                    <strong><u><i>DESCRIPTION:</i></u></strong><xsl:text>  </xsl:text>
                    <xsl:value-of select="description"/> <br />
                    </p>
                    <p>
                    <strong><u><i>LINK:</i></u></strong><xsl:text>  </xsl:text>
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