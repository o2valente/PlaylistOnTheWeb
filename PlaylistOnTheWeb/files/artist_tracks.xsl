<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="root">
        <tbody id="data-table">
            <xsl:for-each select="elem">
               <tr>
                   <xsl:variable name="spotify" select="spotify"/>
                    <td>
                        <img>
                            <xsl:attribute name="src"><xsl:value-of select="url"/></xsl:attribute>
                        </img>
                        <a target="_blank" href="{$spotify}">
                            <xsl:text> </xsl:text><xsl:value-of select="name"/>
                        </a>
                    </td>
                   <td>
                       <xsl:variable name="begin" select="substring(spotify,0,25)"/>
                       <xsl:variable name="end" select="substring(spotify,25)"/>
                       <iframe width="270" height="80" src="{$begin}/embed{$end}"><xsl:comment/></iframe>
                   </td>
                </tr>
            </xsl:for-each>
        </tbody>
    </xsl:template>
</xsl:stylesheet>