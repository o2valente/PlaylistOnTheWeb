<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="root">
        <table id="breadcrumb_album"  class="breadcrumb">

            <tbody>
            <xsl:for-each select="album">
                <tr style="height: 160px;">
                    <th>
                        <img style="width: 120px; height: 120px;">
                            <xsl:attribute name="src">
                                <xsl:value-of select="url"/>
                            </xsl:attribute>
                        </img>
                    </th>
                    <th>
                        <xsl:variable name="spotify" select="spotify"/>
                        <u><i>NAME:</i></u>
                        <a href="{$spotify}" target="_blank">
                            <xsl:text>  </xsl:text>
                            <xsl:value-of select="name"/>
                        </a><br />
                        <i>RELEASE DATE: </i><xsl:value-of select="release_date"/> <br />
                        <i>TOTAL TRACKS: </i><xsl:value-of select="total_tracks"/> <br />
                    <th>
                        <u><i>ARTISTS:</i></u>

                        <xsl:for-each select="artista">
                            <br />
                            <xsl:variable name="id" select="id"/>
                            <a href="http://127.0.0.1:8000/artistTracks?id={$id}" target="_blank">
                                <xsl:value-of select="name"/>
                            </a>

                        </xsl:for-each>
                    </th>
                    </th>
                </tr>
            </xsl:for-each>
            </tbody>
        </table>
    </xsl:template>
</xsl:stylesheet>