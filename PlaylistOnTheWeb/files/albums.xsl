<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="root">
        <ul id="breadcrumb_album">
            <xsl:for-each select="album">
                <li >
                    <img style="width: 120px; height: 120px;">
                        <xsl:attribute name="src">
                            <xsl:value-of select="url"/>
                        </xsl:attribute>
                    </img>
                    <li >
                        <xsl:variable name="spotify" select="spotify"/>
                        <a href="{$spotify}" target="_blank">
                            <xsl:value-of select="name"/>
                        </a>
                        <span>Release Date: <xsl:value-of select="release_date"/> <br /></span>
                        <span> Total Tracks: <xsl:value-of select="total_tracks"/> <br /></span>

                        <xsl:for-each select="artista">
                            <xsl:variable name="id" select="id"/>
                            <a href="http://127.0.0.1:8000/artistTracks?id={$id}" target="_blank">
                                <xsl:value-of select="name"/>
                            </a>
                            <br />
                        </xsl:for-each>
                    </li>
                </li>
            </xsl:for-each>
        </ul>
    </xsl:template>
</xsl:stylesheet>