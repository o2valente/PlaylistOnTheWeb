<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="root">
        <table id="breadcrumb_album"  class="breadcrumb">
            <thead>
                <tr>
                    <th></th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
            <xsl:for-each select="playlistDemo">
                <tr style="height: 130px;">
                    <th style="width: 200px;">
                        <u><i>NAME:</i></u> <xsl:text>  </xsl:text>
                        <xsl:value-of select="nome"/> <br />
                        <u><i>ID:</i></u> <xsl:text>  </xsl:text>
                        <xsl:value-of select="id"/>  <br />
                        <u><i>TRACKS:</i></u> <xsl:text>  </xsl:text>
                        <xsl:value-of select="numeroDeMusicas"/>  <br />
                        <u><i>DATE:</i></u> <xsl:text>  </xsl:text>
                        <xsl:value-of select="dataCriacao"/>
                        </th>
                    <th class="dropdown">

                            <button class="btn btn-outline-success dropdown-toggle" type="button" data-toggle="dropdown">MUSICS
                            <span class="caret"></span></button>
                        <ul class="dropdown-menu">
                        <xsl:for-each select="musicas/musica">
                            <option>
                                <img style="width: 40px; height: 40px;">
                                <xsl:attribute name="src">
                                    <xsl:value-of select="img"/>
                                </xsl:attribute>
                                </img>
                                <xsl:variable name="spotify" select="externalUrl"/>
                                <a href="{$spotify}" target="_blank">
                                    <xsl:text>  </xsl:text>
                                    <xsl:value-of select="nome"/>
                                </a>
                            </option>
                        </xsl:for-each>
                        </ul>

                    </th>
                </tr>
            </xsl:for-each>
            </tbody>
        </table>
    </xsl:template>
</xsl:stylesheet>